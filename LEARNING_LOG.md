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
