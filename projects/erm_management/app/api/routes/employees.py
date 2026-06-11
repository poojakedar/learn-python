from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ... import crud, schemas
from ...db import get_db

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("", response_model=list[schemas.EmployeeOut])
def list_employees(db: Session = Depends(get_db)):
    return crud.list_employees(db)


@router.post("", response_model=schemas.EmployeeOut, status_code=status.HTTP_201_CREATED)
def create_employee(payload: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    if crud.get_employee_by_email(db, payload.email):
        raise HTTPException(status_code=409, detail="Email already exists")
    return crud.create_employee(db, payload)


@router.get("/{employee_id}", response_model=schemas.EmployeeOut)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.put("/{employee_id}", response_model=schemas.EmployeeOut)
def update_employee(employee_id: int, payload: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    if payload.email and payload.email != employee.email:
        if crud.get_employee_by_email(db, payload.email):
            raise HTTPException(status_code=409, detail="Email already exists")

    return crud.update_employee(db, employee, payload)


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    crud.delete_employee(db, employee)
