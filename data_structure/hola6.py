"""file = open("movies.txt","w")
file.write("Top Gun\n")
file.write("MS dhoni\n")
file.write("La la land\n")
file.close()

file = open("movies.txt","r")
data = file.read()
print(data[:10])
file.close()

file = open("movies.txt","r")
data = file.read()
print(data.replace(" ",""))
file.close()

file = open("movies.txt","r")
data = file.read()
print(data.strip())
file.close()


file = open("movies.txt","r")
data = file.read()
words = data.split()
for w in words:
    print(w[::-1])
file.close()
"""


###############Exception Handling####################

"""try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print(a/b)
except:
    print("Bro you got an error!!")"""


try:
    file=open("movies.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:                                #or can write else in place of finally
    print("Program ends")








