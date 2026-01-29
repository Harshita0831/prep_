"""file = open("data1.txt","w")
file.write("My name is Harshita")
file.close()

file = open("data1.txt","r")
data = file.read()
print(data.upper())
file.close()

file = open("data1.txt","r")
data = file.read()
print("characters in the file:",len(data))
file.close()

file = open("data1.txt","r")
data = file.read()
words = data.split()
print("Total no. of words: ",len(words))
file.close()

file = open("data1.txt","r")
data = file.read()
count = data.lower().count("harshita")
print("Word count:",count)
file.close()"""

file = open("data1.txt","r")
data = file.read()
"""s = words[::-1]
print(s)
file.close()"""
data.replace("Harshita","Henry")
print(data)
file.close()
