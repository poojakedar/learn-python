from typing import Optional

from sqlalchemy.orm import Session

from . import models, schemas


# Department CRUD

def list_departments(db: Session):
    return db.query(models.Department).order_by(models.Department.id).all()


def get_department(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id == department_id).first()


def create_department(db: Session, payload: schemas.DepartmentCreate):
    department = models.Department(name=payload.name)
    db.add(department)
    db.commit()
    db.refresh(department)
    return department


def update_department(db: Session, department: models.Department, payload: schemas.DepartmentUpdate):
    if payload.name is not None:
        department.name = payload.name
    db.commit()
    db.refresh(department)
    return department


def delete_department(db: Session, department: models.Department):
    db.delete(department)
    db.commit()


# Employee CRUD

def list_employees(db: Session):
    return db.query(models.Employee).order_by(models.Employee.id).all()


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()


def create_employee(db: Session, payload: schemas.EmployeeCreate):
    employee = models.Employee(
        name=payload.name,
        email=payload.email,
        role=payload.role,
        department_id=payload.department_id,
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def update_employee(db: Session, employee: models.Employee, payload: schemas.EmployeeUpdate):
    updates = payload.model_dump(exclude_unset=True)
    for key, value in updates.items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(db: Session, employee: models.Employee):
    db.delete(employee)
    db.commit()
