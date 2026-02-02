#1. generate random numbers
#2. check which number is even/odd
#3. round umber using math
#4. count how many times numbers appear
#5. save the result in file

#importing libraries
import random
import math
import os
import re
from collections import Counter

#printing random numbers
numbers = [random.randint(1,10) for _ in range(10)]
#even or odd
even_num = []
odd_num = []
for num in numbers:
    num_str = str(num)
    if re.search(r"^[02468]$",num_str):
        even_num.append(num)
    else:
        odd_num.append(num)
#calculate average
average = sum(numbers)/len(numbers)
#round off the average
round_avg = math.ceil(average)
#count numbers
count = Counter(numbers)
#save result using OS
if not os.path.exists("easy_reports"):
    os.mkdir("easy_reports")
#file path
file_path = os.path.join("easy_reports","number_report.txt")
#write data to a file
file = open(file_path,"w")
file.write(f"Generated numbers:{numbers}")
file.write(f"Even numbers:{even_num}")
file.write(f"Odd numbers:{odd_num}")
file.write(f"average:{round_avg}")
file.write(f"number count:\n")
for num, count in count.items():
    file.write(f"{num} -> {int} times\n")
print("Report saved successfully")










"""
n1 = "Rahul"
n2 = " Sharma"
n3 = "".join([n1,n2])
print(n3)
"""
