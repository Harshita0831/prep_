marks = [10,20,30,33]
print(marks[0])

marks.append(100)     #add element in the last of list
print(marks)

marks.insert(1,75)     #insert element on the specified index
print(marks)

marks.insert(2,75)
print(marks)

marks.remove(75)
print(marks)

marks.pop()             #removes last element of list
print(marks)


age = [18,23,45,2,7]
age.sort()
print(age)
age.reverse()
print(age)
print(len(age))
print(sum(age))
print(max(age))
print(sum(age)/len(age))

cities = ["Chhindwara","Delhi","Banaras","Mumbai","Chennai"]
print(cities)
print(len(cities))

cities.append("Barcelona")
print(cities)

cities.remove("Delhi")
print(cities)

cities.insert(1,"Amsterdamn")
print(cities)

print(cities.pop())
print(cities)

#tuple      ##tuple is immutable and is faster tha list
days = ('monday','tuesday','wednesday','thursday','friday')
print(days[0])
print(days[-1])
print(days.index('tuesday'))
print(days[0]=='sunday')
print(len(days))
print(days[1:3])
print('monday' in age)

friends = ['Priya','Harshit','Mansi','Rishika','Kanak']
print(friends[1])
print(friends[-1])
print(friends.index('Mansi'))
print(len(friends))
print(friends[1:3])


#Set            #it is unorde/red
numbers = {10, 20, 30 ,40,10}
print(numbers)
number = {10, 20, 30 ,40}
print(number)
for i in numbers:
    print(i)
numbers.add(100)
numbers.update([120,130])
#numbers.remove(75)         #will give error if element is not present
numbers.discard(175)       #will not give error if element is present or not
numbers.pop()               #will pop random element
print(numbers)


#union
a = {1,2,3}
b = {3,4,5,6}
c = {1,2}
print(a.union(b))
print(a.intersection(b))
print(c.issubset(a))

#os,dbms,dsa,programming,

marks = {79, 85,97,95}
harshita = {78,87,79}
mark = {79,85}
print(marks)

marks.add(100)
print(marks)

print(marks.union(harshita))
print(marks.intersection(harshita))
print(mark.issubset(marks))








