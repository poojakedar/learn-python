from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), unique=True, nullable=False, index=True)

    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False, index=True)
    email = Column(String(200), unique=True, nullable=False, index=True)
    role = Column(String(120), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)

    department = relationship("Department", back_populates="employees")
