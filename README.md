# Healthcare Tech Lab

A learning and portfolio project using synthetic assessment-session data only.
No real patient data or clinical decision-making functionality.

## Current stack and progress

- Verified locally on 2026-10-15: Python 3.11.13, Django 5.2.18,
  pytest 9.1.1 and pytest-django 4.14.0.
- Synthetic session dictionary and basic non-negative answers-count validation.
- Django project `config`, registered app `assessments`, and `/health/` endpoint.
- **4 tests passed**: three count cases and one health endpoint test.
- SQLite is configured; no assessment models or app migrations are implemented.
  Database setup and PostgreSQL remain unverified.

## Setup

From the repository root, with Python 3.11 available:

```bash
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

These create an isolated environment and install the three pinned direct
dependencies. Their versions match the existing environment, and `pip check`
reports no broken requirements. A fresh installation has not been verified.

Commands below explicitly use the project's Python and do not require activation.
With `source .venv/bin/activate`, `python` can replace `.venv/bin/python`.

## Run and test

Start the local Django development server from the repository root:

```bash
.venv/bin/python manage.py runserver
```

Open <http://127.0.0.1:8000/health/>; expect HTTP 200 with `{"status": "ok"}`.
The root path `/` has no route and returns 404. These responses were verified
with Django's test client; browser/server behaviour has not been independently
verified. The health response does not check database connectivity.

Run Django's configuration checks:

```bash
.venv/bin/python manage.py check
```

Verified result: `System check identified no issues (0 silenced).`

Run the automated tests; the development server need not be running:

```bash
.venv/bin/python -m pytest -q
```

Verified result: **4 passed**. `pytest.ini` tells pytest-django to load
`config.settings`. The endpoint test checks HTTP 200 and the exact JSON body;
the count tests cover zero, negative and positive integers, not input types.

Run the original Python example:

```bash
.venv/bin/python src/session_example.py
```

Verified output: `True`, `False`, `True` on separate lines.

## Project structure

- `src/session_example.py`: synthetic dictionary, validation and example prints.
- `src/__init__.py`: marks the source directory as a Python package.
- `manage.py`: Django command entry point.
- `config/settings.py`: settings, installed apps and SQLite configuration.
- `config/urls.py`: `/health/` and Django admin URL mappings.
- `assessments/views.py`: health response; `models.py` is a scaffold only.
- `tests/test_health.py`: health endpoint status and JSON assertions.
- `tests/test_session_example.py`: three validation tests.
- `pytest.ini`: Django settings selection for pytest-django.
- `requirements.txt`: pinned Django, pytest and pytest-django versions.
- `.gitignore`: ignores `.venv/`, `db.sqlite3`, `*.pyc` and `__pycache__/`;
  all four rules were verified with `git check-ignore`.
- `PLAN.md`: stages and next task.
- `LEARNING_LOG.md`: evidence, debugging and practice gaps.
