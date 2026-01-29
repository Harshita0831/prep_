#Dictionary
student = {"Name":"Rahul","Class":12,"City":"Delhi","Course":"python"}
print(student)
print(student["Name"])
print(student.keys())           #print all keys

print(student.values())         #prints all values

print(student.items())          #prints all items in()

print(student.get("Class"))
student["Class"]=11             #updates paticular key
print(student)
student.update({"Name":"Henry","Class":10})    #updates multiple key
print(student)
student["Class"] = 24
print(student)
student.pop("City")                 #deletes particular key
print(student)
student.popitem()                   #deletes last item
print(student)
print(len(student))                     #print length of dict

###
dict1 = {"a":2,"b":3}
dict2 = {"c":4,"d":5}
dict1.update(dict2)         #merges two dict
print(dict1)

#Mobile dict
mobile = {"Brand":"Samsung","Model":"S24","Price":75000,"Stock":20}
print(mobile)
print(mobile["Brand"])
print(mobile.keys())
print(mobile.values())
print(mobile.items())
print(len(mobile))
mobile["Model"]="S25"
print(mobile)
mobile.update({"Price":85000,"Stock":90})
print(mobile)
mobile.pop("Stock")
mobile.popitem()
print(mobile)
mob = {"Store":"Delhi"}
mobile.update(mob)
print(mobile)
print(len(mobile))
mobile.clear()          #deletes the dict
