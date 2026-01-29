"""
#1
print(True+True+False)

#2
print("4"+"4")

#3
print("5"*10)

#4
def change(x):
    x+=10
a=5
change(a)
print(a)            #int is immutable

#5
def update(lst):
    lst.append(10)
nums = [1,2,3]
update(nums)
print(nums)

#6
t = (1,2,3)
t = t+(4,)
print(t)

#7
s = {1,2,2,3,3}
print(len(s))

#8
i = 1
while i<10:
    i*=3
    print(i)  #crazz

#9
for i in range(3):
    print(i)
else:
    print("done")

#10
try:
    print("A")
    10/0
    print("B")
except:
    print("C")
print("D")

#11
try:
    print(1)
except:
    print(2)
finally:
    print(3)

#12
def test():
    try:
        return 10
    finally:
        return 20
print(test())
"""

#Que1           #crazyyy
#move all zeroes to end
nums = [0,1,0,3,12]
result = []         #we will store non zero elements in this
zero_count = 0
for n in nums:
    if n==0:
        zero_count += 1
    else:
        result.append(n)
for i in range(zero_count):
    result.append(0)
print(result)


#Q-2
#Palindrome with two pointer approach
text = "naman"
left = 0
right = len(text) - 1
isPalindrome = True
while left<right:
    if text[left] != text[right]:
        isPalindrome = False
        break
    left+=1
    right-=1
print(isPalindrome)

#Q-3
#longest word in a sentence
sentence = "Python makes problem solving fun"
words = sentence.split()
longest = ""
for i in words:
    if len(i)>len(longest):
        longest = i
print(longest)


#Q-4
#two sum que in dsa
l1 = [1,2,3,2]
target = 5
count = 0
for i in range(len(l1)):
    total = 0
    for j in range(i, len(l1)):
        total+=l1[j]
        if total == target:
            count+=1
print(count)

#Q-4
nums = [2,7,11,15]
target= 9
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        #check if sum matches target
        if nums[i]+nums[j]==target:
            print(nums[i],nums[j])

#two pointers approach
nums = [2,7,11,15]
target = 9
left = 0
right = len(nums)-1
while left<right:
    current_sum = nums[left]+nums[right]
    if current_sum==target:
        print(nums[left], nums[right])
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1
#fast and slow or tortoise and hair technique

nums = [10, 20 ,30, 40,50]
slow = 0
fast = 0
while fast<len(nums) and fast+1<len(nums):
    slow+=1
    fast+=2
print(nums[slow])
























        

































