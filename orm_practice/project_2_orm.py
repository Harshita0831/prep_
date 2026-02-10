#add_category -> add books category
#add_book -> adds new book
#borrow_book -> borrow a book
#update_borrow -> uddate borrow date
#search_by_date -> find borrowed books by date
#category_report -> count borrowed books per category
#set_limit -> set monthly borrow
#limit_alert -> check if limit exceeded

# Used to create database connection and write SQL queries
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text

# Used to define ORM tables and database session
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Creates SQLite database file named libtrack.db
# echo=True prints SQL queries for learning purpose
#data base connection
engine = create_engine("sqlite:///libtrack.db")

# Base class for ORM models
Base = declarative_base()

# Session class (acts like cursor)
Session = sessionmaker(bind = engine)

# Create session object
session = Session()


#Category Table
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)
    name = Column(String)

    # One category → many books
    books = relationship("Book", back_populates = "category")

#Book Table
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    author = Column(String)

    category_id = Column(Integer, ForeignKey("categories.id"))
    
    # Link book to category
    category = relationship("Category" , back_populates = "books")
    
    # One book → many borrows
    borrows = relationship("Borrow", back_populates = "book")


#Borrow Table
class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key = True)
    borrow_date = Column(String)

    book_id = Column(Integer, ForeignKey("books.id"))

    # Link borrow to book
    book = relationship("Book", back_populates = "borrows")

# Monthly limit table
class Limit(Base):
    __tablename__ = "limits"
    id = Column(Integer, primary_key = True)
    month = Column(String)
    max_books = Column(Integer)

# Create tables in database
Base.metadata.create_all(engine)

def add_category():
    name = input("Category name: ")

    #create category object and save
    session.add(Category(name=name))
    session.commit()

    print("Category added")

def add_book():
    title = input("Book Title: ")
    author = input("Author name: ")
    category_id = int(input("Category id: "))

    #create book object
    session.add(Book(title = title, author = author, category_id = category_id))
    session.commit()
    print("Book added")

def borrow_book():
    book_id = int(input("Book ID: "))
    date = input("borrow date (YYYY-MM-DD):")

    #create borrow record
    session.add(Borrow(book_id = book_id, borrow_date = date))
    session.commit()

    print("Book borrowed")

def update_borrow():
    bid = int(input("borrow id: "))
    #find borrow record
    borrow = session.query(Borrow).filter(Borrow.id == bid).first()
    
    if borrow:
        borrow.borrow_date = input("new date: ")
        session.commit()
        print("Borrow updated")
    else:
        print("Borrow not found")

def delete_borrow():
    bid = int(input("Borrow id: "))

    borrow = session.query(Borrow).filter(Borrow.id == bid).first()
    
    if borrow:
        session.delete(borrow)
        session.commit()
        print("Borrow deleted")
    else:
        print("Borrow not found")

def search_by_date():
    date = input("Enter date: ")

    borrows = session.query(Borrow).filter(Borrow.borrow_date == date).all()
    
    for b in borrows:
        print(b.book.title, "-", b.borrow_date)

#SQL REPORT
def category_report():
    sql = text("""SELECT categories.name, COUNT(borrows.id)
    FROM categories
    JOIN books ON categories.id = books.category_id
    JOIN borrows ON books.id = borrows.book_id
    GROUP BY categories.name""")
        
    result = session.execute(sql)

    print("\n Category Wise Borrow Report")
    for row in result:
        print(row[0], "→", row[1])

def set_limit():
    month = input("Month (YYYY-MM): ")
    max_books = int(input("Max books allowed: "))

    session.add(Limit(month=month, max_books=max_books))
    session.commit()

    print("Monthly limit set")


def limit_alert():
    month = input("Month (YYYY-MM): ")

    # Count borrows for month
    total = session.execute(
        text("SELECT COUNT(*) FROM borrows WHERE borrow_date LIKE :m"),
        {"m": f"{month}%"}
    ).scalar()

    limit = session.query(Limit).filter(Limit.month == month).first()

    if limit and total > limit.max_books:
        print("Borrow limit exceeded")
    else:
        print("Within borrow limit")

# ---------- CLI MENU ----------

while True:
    print("""
===== LIBTRACK =====
1. Add Category
2. Add Book
3. Borrow Book
4. Update Borrow
5. Delete Borrow
6. Search Borrow by Date
7. Category Borrow Report
8. Set Monthly Limit
9. Limit Alert
10. Exit
""")

    choice = input("Choose: ")

    if choice == "1":
        add_category()
    elif choice == "2":
        add_book()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        update_borrow()
    elif choice == "5":
        delete_borrow()
    elif choice == "6":
        search_by_date()
    elif choice == "7":
        category_report()
    elif choice == "8":
        set_limit()
    elif choice == "9":
        limit_alert()
    elif choice == "10":
        break
    else:
        print("Invalid choice")