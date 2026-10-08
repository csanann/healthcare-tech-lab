# Healthcare Tech Lab Plan

## Objective

Build a small professional project and practical, interview-ready skills using
synthetic assessment-session data only. Human understanding and review take
priority; AI assists with explanation and repetitive work.

## Verified progress — 2026-10-08

- Python environment configured: Python 3.11.13; `.venv/` correctly gitignored.
- Local Git `main` tracks `origin/main`.
- Synthetic assessment-session dictionary implemented.
- Basic validation checks whether `answers_count` is non-negative.
- Three tests cover zero, negative and positive counts: **3 passed** with
  `.venv/bin/python -m pytest -v` using pytest 9.1.1.
- `requirements.txt` records `pytest==9.1.1`.

Stage 0's Python setup and Stage 1's initial exercise are verified. Fresh
setup and PostgreSQL remain unverified. Broader Python proficiency and
input-type validation still need practice.

## Current stage and next task

Initial Python exercise verified; next: **Stage 2 — Django fundamentals**.
Django has not been installed or implemented.

Next task (HUMAN + AI): select a Django version compatible with Python 3.11,
then create a minimal project in a separate, small increment. Human should
inspect the generated structure and explain:

request → URL routing → view → response

First expected behaviour: a local URL returns a simple non-clinical response.
Record setup and verification before marking this stage complete.

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
