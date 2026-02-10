#creatin a base class
from sqlalchemy.orm import declarative_base
#create table
from sqlalchemy import Column, Integer, String
#insert and add data and commit
from sqlalchemy.orm import sessionmaker
#to connect database
from sqlalchemy import create_engine
from sqlalchemy import or_
from sqlalchemy import desc, asc
from sqlalchemy import ForeignKey
import relationship

#step 1
engine = create_engine("sqlite:///college.db")
#step 2
Base = declarative_base()
class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    student = relationship("Student", back_populates = "departments")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates = "students")

#back_populates - it shows bi directional relationship
