# Week 1 Tasks

## Repository

- [x] Create public GitHub repository named job-tracker
- [x] Clone locally
- [x] Create develop branch from main
- [x] Set branch protection on main: require PR, require status checks to pass (placeholder for now), no direct push
- [x] Create .gitignore — include __pycache__, *.pyc, .env, node_modules, dist, .venv
- [x] Create empty README.md with project title and one-line description
- [x] Commit: chore: initial repo setup
- [x] Invite me as a collaborator on your project. My email is gjoko.pargo@dogon.biz

## Folder scaffold

- [x] Create top-level folders: backend/, frontend/, infra/, docs/, .github/workflows/
- [x] Add a .gitkeep file inside each empty folder so Git tracks them
- [x] Commit: chore: scaffold monorepo folder structure

## Architecture documentation

- [x] Create docs/architecture.md
- [x] Write in plain English (no diagrams yet): what each component is, what it does, how they connect
-  Browser / React SPA
-  Azure Static Web Apps
-  Azure App Service (FastAPI)
-  Azure Container Registry
-  Azure Database for PostgreSQL
-  Azure Blob Storage
- [x] Add a Mermaid flowchart diagram to docs/architecture.md showing the high-level component flow

-  The diagram should look structurally like this — write it yourself in Mermaid syntax:
-  Browser → Static Web Apps → App Service → PostgreSQL
-  → Blob Storage
-  App Service ← Container Registry

- [x] Commit: docs: add architecture documentation and diagram

## Docker Compose — local environment

- [x] Create docker-compose.yml at repo root with:
- [x] postgres:15 service — port 5432:5432, named volume for data persistence, env vars for POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
-  pgadmin service — port 5050:80, depends on postgres
- [x] Run docker compose up -d
- [x] Open pgAdmin at http://localhost:5050, connect to the PostgreSQL instance, confirm the default database exists
- [x] Commit: chore: add docker-compose for local development

## Backend scaffold

- [x] Inside backend/, create pyproject.toml with project name, Python version >=3.12
- [x] Create a Python virtual environment: python -m venv .venv
- [x] Install initial dependencies: fastapi, uvicorn[standard], ruff
- [x] Add them to pyproject.toml under [project.dependencies]
- [x] Create backend/.env.example with placeholder entries:

-  DATABASE_URL=
-  RET_KEY=
-  ENVIRONMENT=development

- [x] Create backend/app/__init__.py and backend/app/main.py with a single line: # TODO
- [x] Run ruff check . from backend/ — should pass with no errors
- [x] Commit: chore(backend): scaffold python project

## Frontend scaffold

- [x] From frontend/, run npm create vite@latest . -- --template react-ts
- [x] Run npm install
- [x] Run npm run build — confirm it succeeds
- [x] Run npx eslint --init and configure for TypeScript + React
- [x] Confirm tsconfig.json has "strict": true
- [x] Delete the boilerplate content in src/App.tsx — replace with <h1>Job Tracker</h1>
- [x] Run npm run dev — confirm it loads in the browser
- [x] Commit: chore(frontend): scaffold vite react typescript project