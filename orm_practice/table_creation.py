#import declarative base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
#step 1
engine=create_engine("sqlite:///school.db")
#create base class
#step 2
Base=declarative_base()
#base will be parent of all models
#step 3
class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    course=Column(String)
#create all tables defined using base
#step 4
Base.metadata.create_all(engine)

#step 5
Session=sessionmaker(bind=engine)
session=Session()
s1=Student(id=6,name="rahul",age=21,course="python")
s2=Student(id=5,name="karan",age=22,course="java")
session.add(s1)
session.add(s2)
session.commit()
students = session.query(Student).all()
for i in students:
    print(i.id,i.name,i.age,i.course)