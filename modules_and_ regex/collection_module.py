##
from collections import Counter
fruit = ["Apple","Banana","Cherry","mango","Banana"]
count = Counter(fruit)
print(count)

##
from collections import Counter
text = "hello"
con = Counter(text)
print(con)

##
from collections import Counter
sen = "Python is easy and Python is powerful"
cont = Counter(sen.split())
print(cont)

##
num = [1,2,3,4,3,1,2,4,3,2]
c = Counter(num)
print(c)

##
import os
current_path = os.getcwd()
print(current_path)

##
item = os.listdir()
print(item)
##
folder = "Harshita"
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created successfully")

##
file = "collection_module"
if not os.path.exists(file):
    print("exist")
else:
    print("not")









    
