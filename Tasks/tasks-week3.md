# Tasks

## App configuration

- [x] Install pydantic-settings  
- [x] Create backend/app/core/config.py:

Python

  from pydantic_settings import BaseSettings

  class Settings(BaseSettings):
      DATABASE_URL: str
      SECRET_KEY: str
      ENVIRONMENT: str = "development"

      model_config = ConfigDict(env_file=".env")

  settings = Settings()

- [x] Commit: feat(backend): add pydantic settings config

## Database session dependency

- [ ] Create backend/app/core/dependencies.py  
- [ ] Add get_db async generator dependency that yields a SQLAlchemy AsyncSession and closes it after the request  
- [ ] Commit: feat(backend): add database session dependency

## Layer structure

- [ ] Create empty __init__.py files to establish the package structure:
  - [ ] backend/app/api/__init__.py  
  - [ ] backend/app/api/v1/__init__.py  
  - [ ] backend/app/api/v1/endpoints/__init__.py  
  - [ ] backend/app/repositories/__init__.py  
  - [ ] backend/app/schemas/__init__.py  
  - [ ] backend/app/services/__init__.py  
- [ ] Create backend/app/api/v1/router.py — empty APIRouter for now  
- [ ] Commit: chore(backend): establish layer package structure

## Health endpoint

- [ ] Create backend/app/api/v1/endpoints/health.py  
- [ ] Implement GET /api/v1/health:
  - [ ] Returns {"status": "ok"} when DB is reachable  
  - [ ] Returns {"status": "degraded", "detail": "database unreachable"} with HTTP 503 if DB connection fails  
- [ ] Test the degraded case by stopping the Docker PostgreSQL container temporarily  
- [ ] Register the router in main.py with prefix /api/v1  
- [ ] Start the server: uvicorn app.main:app --reload  
- [ ] Confirm GET http://localhost:8000/api/v1/health returns 200  
- [ ] Confirm GET http://localhost:8000/docs shows the Swagger UI  
- [ ] Commit: feat(backend): add health check endpoint

## Custom exceptions

- [ ] Create backend/app/core/exceptions.py:

python

  class NotFoundError(Exception): ...
  class ForbiddenError(Exception): ...
  class ConflictError(Exception): ...
  class ValidationError(Exception): ...

- [ ] Register global exception handlers in main.py that convert each to the appropriate HTTP response  
- [ ] Commit: feat(backend): add custom exceptions and global handlers

## CORS configuration

- [ ] Add fastapi.middleware.cors.CORSMiddleware to main.py  
- [ ] Allow origins: http://localhost:5173 (Vite dev server) for development  
- [ ] Read the allowed origin from settings — not hardcoded  
- [ ] Commit: feat(backend): add cors middleware

## First pytest test

- [ ] Install pytest, pytest-asyncio, httpx  
- [ ] Create backend/tests/conftest.py with an AsyncClient fixture pointing at the FastAPI app  
- [ ] Create backend/tests/test_health.py:
  - [ ] Test: GET /api/v1/health returns 200 and {"status": "ok"}  
- [ ] Run pytest — confirm it passes  
- [ ] Commit: test(backend): add health endpoint test

## Ruff configuration

- [ ] Add [tool.ruff] section to pyproject.toml:

toml

  [tool.ruff]
  line-length = 88
  target-version = "py312"

  [tool.ruff.lint]
  select = ["E", "F", "I", "UP"]

- [ ] Run ruff check . from backend/ — fix any issues  
- [ ] Run ruff format . — auto-format all files  
- [ ] Commit: chore(backend): configure ruff and apply formatting

## Week 3 — Definition of Done

- [ ] GET /api/v1/health returns 200 with DB running, 503 with DB stopped  
- [ ] Swagger UI is accessible at /docs  
- [ ] Layer structure exists as packages (even if mostly empty)  
- [ ] Custom exceptions are defined and registered  
- [ ] At least one pytest test passes  
- [ ] ruff check . passes with zero errors