from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ... import crud, schemas
from ...db import get_db

router = APIRouter(prefix="/departments", tags=["departments"])


@router.get("", response_model=list[schemas.DepartmentOut])
def list_departments(db: Session = Depends(get_db)):
    return crud.list_departments(db)


@router.post("", response_model=schemas.DepartmentOut, status_code=status.HTTP_201_CREATED)
def create_department(payload: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db, payload)


@router.get("/{department_id}", response_model=schemas.DepartmentOut)
def get_department(department_id: int, db: Session = Depends(get_db)):
    department = crud.get_department(db, department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


@router.put("/{department_id}", response_model=schemas.DepartmentOut)
def update_department(department_id: int, payload: schemas.DepartmentUpdate, db: Session = Depends(get_db)):
    department = crud.get_department(db, department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return crud.update_department(db, department, payload)


@router.delete("/{department_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    department = crud.get_department(db, department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    crud.delete_department(db, department)
