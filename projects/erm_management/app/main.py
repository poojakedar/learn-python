from fastapi import FastAPI

from .api.routes import departments, employees
from .db import Base, engine

app = FastAPI(title="ERM Management API", version="1.0.0")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(departments.router)
app.include_router(employees.router)
