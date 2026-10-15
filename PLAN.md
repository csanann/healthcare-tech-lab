# Healthcare Tech Lab Plan

## Objective

Build a small professional project and practical, interview-ready skills using
synthetic assessment-session data only. Human understanding and review take
priority; AI assists with explanation and repetitive work.

## Verified progress — 2026-10-15

- Python environment configured: Python 3.11.13; `.venv/` correctly gitignored.
- Synthetic assessment-session dictionary implemented.
- Basic validation checks whether `answers_count` is non-negative.
- Django 5.2.18 project `config` and registered app `assessments` implemented.
- `/health/` resolves to `assessments.views.health_check` and returns HTTP 200
  with `{"status": "ok"}`; `/` returns 404. Verified using Django's test client.
- `pytest.ini` selects `config.settings`; pytest-django initializes Django.
- **4 passed** with `.venv/bin/python -m pytest -q`: zero, negative and positive
  count tests, plus the health endpoint test.
- `.venv/bin/python manage.py check` reports no issues.
- `requirements.txt` pins Django 5.2.18, pytest 9.1.1 and pytest-django 4.14.0;
  all match installed versions. `pip check` reports no broken requirements.
- `.gitignore` rules verified for `.venv/`, `db.sqlite3`, `*.pyc` and
  `__pycache__/`.

The initial Python exercise and Django health endpoint work in the existing
environment. Fresh installation, browser/server behaviour, migrations and
database connectivity remain unverified. SQLite is configured; no assessment
models or app migration files exist beyond the migrations package initializer.
Passing tests do not establish independent human understanding or input-type
validation.

## Current stage and next task

**Stage 2 — Django fundamentals, in progress.** The first endpoint and its
automated test are implemented and verified; the learning stage is not complete.

Next task (HUMAN + AI): human traces `/health/` through `config/urls.py`,
`assessments/views.py` and `tests/test_health.py`, then explains:

- Request path → matching URL pattern → view → JSON response.
- Why `/` returns 404 even when Django's configuration checks pass.
- Why pytest needs Django settings and what the two endpoint assertions prove.

Small debugging exercise: temporarily change the test's expected status to
201, predict the failure, run that test, then restore 200. AI reviews the
explanation and result before moving to database models. This exercise has
not yet been attempted or verified.

## Later stages

3. PostgreSQL and models: verify database setup, then relationships and migrations.
4. Validation: input types, boundaries and database constraints.
5. SQL: query synthetic data through SQL and the Django ORM.
6. Testing: extend existing practice to models and application behaviour.
7. API: after Django and data fundamentals are understood.
8. Docker: after local application and database behaviour are understood.
9. CI: automate relevant checks and tests.

Continue Python practice as needed: collections, loops, modules, exceptions,
classes and type hints. Assess explanation and debugging, not only working code.

## Explicit non-goals

- Real patient information, clinical scoring, diagnosis or treatment advice.
- Cloud or production deployment, AI features and complex frontend work.
