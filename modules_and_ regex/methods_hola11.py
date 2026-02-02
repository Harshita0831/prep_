import math
num = 16
result = math.sqrt(num)
print(result)

##
import math
num = 7.8
print(math.floor(num))
print(math.ceil(num))

##
import math
result = math.pow(2,3)
print(result)

##
import random
dice = random.randint(1,6)
print(dice)

##
print(random.randint(1,100))

##
import random
student = ["Henry","Harry","ben","Neha"]
selected = random.choice(student)           #used for data structures
print("Congratulations",selected)

##
import random
print(random.randint(1000,9999))

##
import datetime
current = datetime.datetime.now()
print(current)
today = datetime.date.today()
print(today)
print(current.date())
print(current.month)
print(current.year)

##
date = datetime.date(2026,1,1)
date1 = datetime.date(2026,1,28)
print(date)
print(date1)
print(date1-date)























