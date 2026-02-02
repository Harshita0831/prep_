#1. write regex pattern to detect 10-digit mobile no.
import re               #regex imported
mobile = "8690134567"
pattern = r"^[0-9]{10}$"
if re.match(pattern,mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")

#2. extract email from the string
sen = "contact me at test@gmail.com or admin@yahoo.in"
result = re.findall("test@gmail.com?",sen)
result1 = re.findall("admin@yahoo.in",sen)
print(result)
print(result1)
#pattern to find gmail 
#r"[\w.-]+@[\w.-]+\.\w+"
#r is telling that it is not a simple code it is calleing regex function
res = r"[\w.-]+@[\w.-]+\.\w+"
email = re.findall(res,sen)
print(email)

#3. extract all number from string
str = "Order123 price45 quantity6"
rest = re.findall(r"\d+",str)
print(rest)


#4. Validate a strong password
#at least 8 characters
#one uppercase and lowercase
#one digit and special character

str1 = "Henry$100"
pattern = re.findall(r"\w+",str1)
pat = re.findall(r"\d",str1)
print(pattern)
print(pat)

#5. Evaluate pan number
str1 = "ABCDE1234F"
pat = re.findall(r"[A-Z]+",str1)
pat1 = re.findall(r"\d{4}",str1)
pat2 = re.findall(r"\D+$",str1)
print(pat)
print(pat1)
print(pat2)

#6. evaluate ipv4
st = "185.107.106.777"
pat = re.findall(r"\d+",st)
print(pat)

#7. evaluate ipv6
str1 = "2001:db8::8a2e:370:7334"
pat = re.findall(r"\d+",str1)
pat1 = re.findall(r"\D+",str1)
print(pat)
print(pat1)

#8. evaluate hexadecimal code
str1 = "#FF0000"
pat = re.findall(r"\d+",str1)
pat1 = re.findall(r"\D+",str1)
pat2 = re.search(r"[@$!%*?&]", str1)
print(bool(pat2))
print(pat)
print(pat1)









