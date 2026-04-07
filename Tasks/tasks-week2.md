# Week 2 Tasks

## ER Diagram

- [ ] On paper (or any whiteboard tool), draw all entities and their relationships before opening a code editor
  - [ ] Identify every table
  - [ ] Identify every foreign key relationship
  - [ ] Mark which relationships are one-to-many
- [ ] Create docs/db-schema.md
- [ ] Write a plain English description of every table: what it represents, why it exists
- [ ] Add a Mermaid ER diagram to docs/db-schema.md covering all 7 tables with their columns and relationships

Your Mermaid ER diagram should use erDiagram syntax. Example structure (you write the full version):

mermaid

erDiagram
    users ||--o{ applications : "owns"
    applications }o--|| companies : "applies to"
    applications ||--o{ status_history : "has"

- [ ] Commit: docs: add database schema documentation and ER diagram

---

## SQLAlchemy models

- [ ] Install dependencies: sqlalchemy[asyncio], asyncpg, alembic
- [ ] Create backend/app/db/base.py — declarative base class
- [ ] Create backend/app/db/session.py — async engine + session factory reading DATABASE_URL from env
- [ ] Create model files for all 7 tables:
  - [ ] backend/app/db/models/user.py
  - [ ] backend/app/db/models/company.py
  - [ ] backend/app/db/models/application.py
  - [ ] backend/app/db/models/status_history.py
  - [ ] backend/app/db/models/contact.py
  - [ ] backend/app/db/models/document.py
  - [ ] backend/app/db/models/reminder.py
- [ ] Each model must include: correct column types, foreign keys, indexes as per schema spec in PROJECT_PLAN.md, created_at with server_default=func.now()
- [ ] Define the ApplicationStatus enum in Python (used in both the model and Pydantic schemas later)
- [ ] Commit: feat(db): add sqlalchemy models for all entities

---

## Alembic setup + first migration

- [ ] Run alembic init alembic inside backend/
- [ ] Edit alembic/env.py:
  - [ ] Import all models so Alembic can detect them
  - [ ] Read DATABASE_URL from environment (use python-dotenv to load .env locally)
  - [ ] Configure async engine usage
- [ ] Create .env in backend/ (do not commit — it's in .gitignore):
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/jobtracker

- [ ] Run alembic revision --autogenerate -m "create_initial_tables"
- [ ] Review the generated migration file — confirm all tables, columns, foreign keys, and indexes are present
- [ ] Run alembic upgrade head
- [ ] Open pgAdmin and verify all 7 tables exist with the correct columns
- [ ] Commit: feat(db): add alembic config and initial migration

---

## Seed script

- [ ] Create backend/app/db/seed.py
- [ ] Script should create:
  - [ ] 1 user (email + hashed placeholder password)
  - [ ] 3 companies
  - [ ] 5 applications across those companies with varying statuses
  - [ ] At least 2 status_history entries per application
  - [ ] 2 contacts
  - [ ] 2 reminders
- [ ] Run the seed script, verify data in pgAdmin
- [ ] Commit: chore(db): add seed script for local development

---

## What I expect by the end of this week:

- [ ] docs/db-schema.md contains a rendered Mermaid ER diagram with all 7 tables
- [ ] All 7 SQLAlchemy models are written and match the schema spec
- [ ] alembic upgrade head runs against the local Docker PostgreSQL with zero errors
- [ ] All 7 tables are visible in pgAdmin with correct columns
- [ ] Seed script populates the database without errors
- [ ] You can explain why status_history is a separate table and what would be lost without it