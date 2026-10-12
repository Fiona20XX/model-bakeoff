import textwrap

import pytest

from bakeoff.task import TaskError, load_task, parse_vars, substitute


def write_task(tmp_path, body: str):
    path = tmp_path / "task.yaml"
    path.write_text(textwrap.dedent(body))
    return path


BASE = """
name: t
user: |
  {user}
models: [a/model, b/model]
judge: j/model
rubric:
  - {{name: x, weight: 0.5}}
  - {{name: y, weight: 0.5}}
"""


def test_var_substitution(tmp_path):
    path = write_task(tmp_path, BASE.format(user="Brief on {{var:company}}."))
    task = load_task(path, {"company": "Stripe"})
    assert task.user.strip() == "Brief on Stripe."
    assert task.vars == {"company": "Stripe"}


def test_missing_var_names_the_variable(tmp_path):
    path = write_task(tmp_path, BASE.format(user="Brief on {{var:company}}."))
    with pytest.raises(TaskError, match="company"):
        load_task(path, {})


def test_file_substitution_relative_to_task_dir(tmp_path, monkeypatch):
    (tmp_path / "notes.md").write_text("NOTES BODY")
    path = write_task(tmp_path, BASE.format(user="Context: {{file:notes.md}}"))
    monkeypatch.chdir(tmp_path.parent)
    assert "Context: NOTES BODY" in load_task(path).user


def test_missing_file_is_an_error(tmp_path):
    path = write_task(tmp_path, BASE.format(user="{{file:nope.md}}"))
    with pytest.raises(TaskError, match="nope.md"):
        load_task(path)


def test_inserted_file_contents_are_not_rescanned(tmp_path):
    (tmp_path / "f.md").write_text("literal {{var:not_a_var}}")
    out = substitute("{{file:f.md}}", {}, [tmp_path])
    assert out == "literal {{var:not_a_var}}"


def test_system_prompt_is_substituted(tmp_path):
    body = BASE.format(user="hi") + "system: You research {{var:company}}.\n"
    task = load_task(write_task(tmp_path, body), {"company": "Acme"})
    assert task.system == "You research Acme."


def test_parse_vars():
    assert parse_vars(["company=Stripe", "q=a=b"]) == {"company": "Stripe", "q": "a=b"}
    with pytest.raises(TaskError):
        parse_vars(["nope"])


def test_rubric_weights_must_sum_to_one(tmp_path):
    body = BASE.format(user="hi").replace("weight: 0.5}", "weight: 0.4}", 1)
    with pytest.raises(TaskError, match="sum to 1"):
        load_task(write_task(tmp_path, body))


def test_hello_task_loads():
    task = load_task("tasks/hello.yaml")
    assert task.models and task.judge and not task.web.enabled
