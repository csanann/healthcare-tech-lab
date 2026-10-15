# Learning Log

## 2026-10-04 — Development Environment

### Practised
- Git repository setup
- Python environment identification
- PATH basics
- Python virtual environments
- Git ignore rules

### Previously recorded understanding (not reassessed here)
- Difference between system Python, Homebrew Python and a project virtual environment
- Why project dependencies should be isolated
- Why `.venv` should not be committed to Git

### Debugging encountered
`python3` initially resolved to Apple's Python 3.9 rather than Homebrew Python 3.11.

Used `which`, `brew --prefix` and version checks to identify the different installations.

### Extra Note is in Obsidian

### Revisit
- Dependency tracking
- Python package management

## 2026-10-08 — Python exercise, testing and dependencies

### Implemented and verified

- Synthetic assessment-session dictionary and `is_valid_answers_count(count)`,
  which checks `count >= 0`.
- Three tests: zero, negative and positive counts.
- Direct dependency recorded as `pytest==9.1.1` in `requirements.txt`.
- AI ran `.venv/bin/python -m pytest -v`: **3 passed** on Python 3.11.13
  with pytest 9.1.1. `.venv/` is confirmed gitignored.

### Demonstrated skills

- Repository evidence: dictionary literals, a Boolean-returning function,
  a local module import and three pytest assertions.
- Human reported resolving `Errno 2` by changing to the project root:
  relative paths depend on the terminal's working directory.
- Human created the requirements file and ran
  `python -m pip install -r requirements.txt`; reported output confirmed
  packages were already installed in `.venv`.

### Debugging and topics still needing practice

- Git merge previously waited for its commit message; AI completed it.
  Practise `git status` and exiting vi with Esc, `:wq`, Enter independently.
- Distinguish `python --version` / `-V` from verbose logging with `-v`.
- Explain why zero is valid and negatives are invalid. Three passing cases
  do not establish behaviour for strings, floats, booleans or missing values.
- Importing the module executes its top-level example prints; revisit
  separating demonstration execution from reusable functions.
- Fresh environment recreation and PostgreSQL setup remain unverified.
- Broader Python fundamentals and independent code explanation need assessment.

### Interview evidence and next step

- Evidence: a synthetic dictionary, non-negative validation and three passing
  tests. Independent explanation has not yet been assessed.
- Practice question: What do these tests prove, and which invalid inputs
  do they leave unchecked?
- Next: Django project structure and request → URL → view → response,
  in a small increment before introducing database models.

## 2026-10-15 — Django routing, endpoint testing and dependency tracking

### Practised and implemented

- Human registered `assessments` in `INSTALLED_APPS`, implemented
  `health_check` returning `JsonResponse({"status": "ok"})`, and mapped
  `path('health/', health_check, name='health_check')` in `config/urls.py`.
- Human wrote `tests/test_health.py`, asserting HTTP 200 and the exact JSON.
- AI created root `pytest.ini` at the human's request, selecting
  `DJANGO_SETTINGS_MODULE = config.settings`.
- `requirements.txt` now contains three valid, unique pins matching installed
  versions: Django 5.2.18, pytest 9.1.1 and pytest-django 4.14.0.
- AI added `db.sqlite3`, `*.pyc` and `__pycache__/` to `.gitignore` at the
  human's request, preserving `.venv/`.

### Debugging encountered and resolved

- Human reported running `check` and `runserver`, then confirmed the failing
  browser URL was `/`. That path has no route; `/health/` is the registered path.
- Initial pytest run was reproduced: **1 failed, 3 passed**. `client.get`
  raised `ImproperlyConfigured` for `DEFAULT_CHARSET` before either assertion.
  At that point pytest-django was absent and pytest had no settings configuration.
  `manage.py` selects `config.settings`; plain pytest does not execute it.
- After pytest-django was installed and `pytest.ini` added, all four tests passed.
- Initial dependency edits duplicated pytest and used an invalid
  `<installed version>` placeholder. Current file has neither issue.

### Verification repeated by AI on 2026-10-15

- `.venv/bin/python -m pytest -q`: **4 passed**.
- `.venv/bin/python manage.py check`: no issues, zero silenced.
- `.venv/bin/python -m pip check`: no broken requirements.
- Python version: 3.11.13. All three installed dependency versions match the pins.
- Django's test client: `/health/` resolves to `assessments.views.health_check`
  and returns HTTP 200 with the expected JSON; `/` returns HTTP 404.
- `.venv/bin/python src/session_example.py`: `True`, `False`, `True`.
- `git check-ignore` confirms all four ignore patterns match example paths.

### Evidence of understanding and limits

- Repository evidence: the human-authored view, route and endpoint test; human
  supplied the exact failing URL when asked. Independent explanation of request
  flow, pytest setup and assertion coverage has not yet been assessed.
- Running browser/server behaviour, fresh environment recreation, migrations,
  database connectivity and PostgreSQL setup have not been independently verified.
- SQLite is configured, but assessment models and app migrations are not
  implemented. The health response does not test database access.
- Count tests establish three integer cases, not validation of strings, floats,
  booleans or missing values. Broader Python proficiency remains to assess.

### Interview practice and next task

- Explain request → URL pattern → view → response using `/health/` and why
  `/` returns 404 despite a successful configuration check.
- Explain why pytest needs settings configuration and why its client needs no
  running server. Distinguish setup exceptions from failed assertions.
- Next exercise: predict the result of expecting HTTP 201 in the endpoint test,
  run that test, and restore 200. Exercise and explanation remain pending.
