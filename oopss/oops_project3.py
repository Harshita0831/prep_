##Design a console based library management system
#a libraryitem is the base(abstract) idea
#book and magazine are different type of items
#borrowing rules behave diff for each of them
#a libraryApp controls items(HAS-A)
#use oops concept and return value, not only print

##
#Create a Library Management System where different library items calculate borrowing charges differently.
#Library item (parent class)
#Book and magazie (child class)
#LibraryApp(main class)

#Book IS-A libraryitem
#Magazine IS-A libraryitem
#LibraryApp HAS-A libraryitem

#Output format
#Item Type: Book
#Borrow Days: 5
#Borrowing Charge: 50
#Or 
#Item Type: Magazine
#Borrow Days: 3
#Borrowing Charge: 30

class LibraryItem:
    def __init__(self,borrow_days):
        self._borrow_days = borrow_days
        
    def calculate_borrowcharge(self):
        pass
    def item_type(self):
        pass
    
class Book(LibraryItem):
    def calculate_borrowcharge(self):
        return self._borrow_days*10
    
    def item_type(self):
        return "Book"
    
class Magazine(LibraryItem):
    def calculate_borrowcharge(self):
        return self._borrow_days*20
    
    def item_type(self):
        return "Magazine"

class LibraryApp:
    def __init__(self,libraryitem):
        self.libraryitem = libraryitem
        
    def borrow_details(self):
        itemtype = self.libraryitem.item_type()
        days = self.libraryitem._borrow_days
        charges = self.libraryitem.calculate_borrowcharge()
        return itemtype,days,charges
obj = Book(5)
app = LibraryApp(obj)
item,days,charges = app.borrow_details()
print("Item type:",item)
print("Borrow Days:",days)
print("Borrowing Charge:",charges)
    
obj1 = Magazine(3)
app1 = LibraryApp(obj1)
item,days,charges = app1.borrow_details()
print("Item type:",item)
print("Borrow Days:",days)
print("Borrowing Charge:",charges)
        























