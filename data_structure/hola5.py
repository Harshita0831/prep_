##String Manipulation
s = "Python Programming"
print(s)
print(len(s))
print(s[0])
print(s[-1])
print(s[:4])
print(s.upper())
print(s)
print(s.strip())
print(s.replace("Python","Java"))
print(s.find("o"))
word = s.split()
print(word)
a = "abs1"
print(a.isalpha())
print(a.isdigit())
b="123"
print(b.isalpha())
print(b.isdigit())
print(s.count("P"))
print(s)
print(s.startswith("Py"))
print(s.endswith("ing"))
print(a.isalnum())
print(s[::-1])
count = 0
for i in s:
    if i in "aeiou":
        count+=1
    print(count)

############Palindrome
h = "madam"
b = h[::-1] 
print(b)
if b == h:
    print("Yes")
else:
    print("No")

S = "apple"
for ch in S:
    print(ch,":",S.count(ch))


###replace vowel with star
s = "Python"
result=""
for ch in s:
    if ch in "aeiou":
        result+="*"
    else:
        result+=ch
    print(result)o
