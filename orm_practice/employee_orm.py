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

#step 1
engine = create_engine("sqlite:///company.db")
#step 2
Base = declarative_base()
#step 3
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)

#step 4
Base.metadata.create_all(engine)

#step 5
Session = sessionmaker(bind = engine)
session = Session()
e1 = Employee(name = "Henry", age = 14, department = "Collector")
e2 = Employee(name = "Dekisuki", age = 19, department = "peon")
session.add(e1)
session.add(e2)
session.commit()

#step 6
employees = session.query(Employee).all()
for i in employees:
    print(i.id, i.name, i.age, i.department)

#to fetch query
# employees = session.query(Employee).filter_by(id=1).first()
# employees.name = "Gian"
# session.commit()
# print("Employee updated")
# employees = session.query(Employee).all()
# for i in employees:
#     print(i.id, i.name, i.age, i.department)

# emp = session.query(Employee).filter(Employee.id == 2).first()
# if emp:
#     session.delete(emp)
#     session.commit()
# print("id deleted")
# employees = session.query(Employee).all()
# for i in employees:
#     print(i.id, i.name, i.age, i.department)

# emp = session.query(Employee).filter(Employee.age> 18).all()
# session.commit()
# print("above 18 deleted")
# employees = session.query(Employee).all()
# for i in employees:
#     print(i.id, i.name, i.age, i.department)

#empp = session.query(Employee)
emp = session.query(Employee).filter(Employee.age>18).all()
for i in emp:
    session.delete(i)
    
session.commit()

#name is rahul or age > 21
emp = session.query(Employee).filter(or_(Employee.name=="Rahul", Employee.age>21)).all()

#name is rahul and age > 21
emp = session.query(Employee).filter(Employee.name=="Rahul", Employee.age>21).all()

emp = session.query(Employee).filter(Employee.name=="Rahul", Employee.age>21).one_or_none()

emp = session.query(Employee).order_by(Employee.id).all()

emp = session.query(Employee).order_by(desc(Employee.id)).all()

#using limit
emp = session.query(Employee).order_by(Employee.id).limit(2).all()
#.all() -> all employees should present
#.first() -> first employee in the list
#.one() -> only one exactly one employee matches
#.one_or_none() -> zero or one allowed #it wont give error 
#.order_by()
#off_set(2) will remove above two rows and give rest
