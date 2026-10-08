# Healthcare Tech Lab

A learning and portfolio project using synthetic assessment-session data only.
No real patient data or clinical decision-making functionality.

## Current stack and progress

- Python 3.11 (verified locally: 3.11.13), pytest 9.1.1, Git and VS Code.
- Synthetic session dictionary and basic non-negative answers-count validation.
- Three tests passed on 2026-10-08: zero, negative and positive counts.
- Next: Django fundamentals. Django is not installed or implemented.
- PostgreSQL is planned; its setup was not verified in this review.

## Setup

From the repository root, with Python 3.11 available:

```bash
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

These create an isolated environment and install the recorded dependency.
`.venv/` is gitignored. The existing environment was verified; fresh setup
has not yet been verified.

## Run and test

```bash
.venv/bin/python src/session_example.py
.venv/bin/python -m pytest -v
```

The example prints `True`, `False`, `True`. Tests check three count cases;
they do not establish input-type validation.

## Project structure

- `src/session_example.py`: synthetic dictionary, validation and example prints.
- `src/__init__.py`: marks the source directory as a Python package.
- `tests/test_session_example.py`: three validation tests.
- `requirements.txt`: direct dependency pin, `pytest==9.1.1`.
- `PLAN.md`: stages and next task.
- `LEARNING_LOG.md`: evidence, debugging and practice gaps.
