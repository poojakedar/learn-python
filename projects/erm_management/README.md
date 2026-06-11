# ERM Management API (Python)

Small Employee Resource Management API using FastAPI + SQLAlchemy + PostgreSQL.

## Features

- DB connection with SQLAlchemy session handling
- Department CRUD APIs
- Employee CRUD APIs
- Basic validations (unique email)
- Health endpoint

## Project Structure

- app/main.py: FastAPI app and router wiring
- app/db.py: database engine, session, base model
- app/models.py: SQLAlchemy models
- app/schemas.py: request/response schemas
- app/crud.py: database operations
- app/api/routes/: API endpoints

## Prerequisites

1. PostgreSQL installed and running (default port 5432)
2. Database created: `createdb erm_db`
3. User: `postgres` with password `password` (or update .env)

## Setup

From this folder (`projects/erm_management`):

1. Copy `.env.example` to `.env` and update PostgreSQL credentials if needed:

```bash
cp .env.example .env
```

2. Install Python dependencies:

```powershell
& "c:/python/.venv-1/Scripts/python.exe" -m pip install -r requirements.txt
```

3. (Optional) Update `.env` with your PostgreSQL credentials if different from defaults:

```
DATABASE_URL=postgresql://YOUR_USER:YOUR_PASSWORD@localhost:5432/erm_db
```

## PostgreSQL Setup (Windows)

1. Download PostgreSQL from https://www.postgresql.org/download/windows/
2. Run installer (default: port 5432, user: postgres)
3. Create database:

```bash
createdb -U postgres erm_db
```

4. Verify connection:

```bash
psql -U postgres -d erm_db
```

## Run API

```powershell
& "c:/python/.venv-1/Scripts/python.exe" -m uvicorn app.main:app --reload --port 8001
```

## API Endpoints

- GET /health
- GET /departments
- POST /departments
- GET /departments/{id}
- PUT /departments/{id}
- DELETE /departments/{id}
- GET /employees
- POST /employees
- GET /employees/{id}
- PUT /employees/{id}
- DELETE /employees/{id}

## Quick Test Payloads

Create department:

```json
{
  "name": "Engineering"
}
```

Create employee:

```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "role": "Backend Engineer",
  "department_id": 1
}
```
