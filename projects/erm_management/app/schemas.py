from typing import Optional

from pydantic import BaseModel, EmailStr


class DepartmentBase(BaseModel):
    name: str


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(BaseModel):
    name: Optional[str] = None


class DepartmentOut(DepartmentBase):
    id: int

    class Config:
        from_attributes = True


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    role: str
    department_id: Optional[int] = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    department_id: Optional[int] = None


class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
