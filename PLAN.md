# Healthcare Tech Lab Plan

## Objective

Build a small healthcare software project while developing practical,
interview-ready junior software engineering skills.

The project uses synthetic assessment-session data only.

## Learning Strategy

Learn through building.

Human focuses on:
- understanding
- decisions
- debugging
- review
- testing
- explanation

AI assists with:
- boilerplate
- repetitive implementation
- review
- test scaffolding
- documentation
- explanations

AI must not replace understanding of core concepts.

---

## Stage 0 — Development Environment

Status: IN PROGRESS

Goal:
Create a clean, reproducible local development environment.

Tasks:
- verify macOS development tools
- configure supported Python
- create Python virtual environment
- verify PostgreSQL
- initialise Git
- configure .gitignore
- establish repository documentation

Evidence:
I can explain what Python environment the project uses and why.

---

## Stage 1 — Python Refresh

Goal:
Refresh only the Python needed for the project.

Practise:
- variables and types
- lists/dictionaries
- functions
- conditionals
- loops
- classes where relevant
- exceptions
- modules/imports
- type hints

Use small healthcare-related synthetic examples.

Evidence:
I can read and modify the Python used by the application.

---

## Stage 2 — Django Fundamentals

Goal:
Understand how a Django application works.

Build:
- Django project
- small assessment application
- URL
- view
- template or simple response
- settings/configuration

Understand:

request
→ URL routing
→ view
→ application logic
→ response

---

## Stage 3 — PostgreSQL + Django Data Model

Create synthetic:

AssessmentSession

Possible fields will be designed before implementation.

Learn:
- models
- field types
- primary keys
- migrations
- ORM
- PostgreSQL tables

Understand:

Django model
→ migration
→ PostgreSQL table
→ ORM query

---

## Stage 4 — Validation

Add realistic non-clinical validation.

Learn:
- application validation
- database constraints
- invalid input
- useful errors
- boundary cases

---

## Stage 5 — SQL Practice

Query the same data using:

1. Django ORM
2. SQL directly

Practise:
- SELECT
- WHERE
- ORDER BY
- COUNT
- GROUP BY
- JOIN when relationships are introduced

Goal:
Understand what the ORM is doing rather than treating it as magic.

---

## Stage 6 — Testing

Add:
- model tests
- validation tests
- query tests
- application behaviour tests

Learn:
Arrange → Act → Assert

Goal:
Explain what each test proves and what it does not prove.

---

## Stage 7 — API

Only after the underlying Django/data concepts are understood.

Expose selected assessment-session functionality through a small API.

---

## Stage 8 — Docker Fundamentals

Containerise the application and PostgreSQL after I understand how they
work locally.

Goal:
Understand the problem Docker solves rather than using it blindly.

---

## Stage 9 — CI

Add a small CI pipeline that automatically runs project quality checks
and tests.

Goal:
Understand:

code change
→ push
→ automated checks
→ pass/fail evidence

---

## Explicit Non-Goals For Now

- clinical scoring
- diagnosis
- treatment recommendations
- real patient information
- production deployment
- cloud architecture
- AI/LLM functionality
- complex frontend

---

## Current Task

Complete Stage 0.

Next:
Choose and configure the project's Python version.