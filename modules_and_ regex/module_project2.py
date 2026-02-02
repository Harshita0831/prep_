#generate random password
#check password strength
#count character used in password
#give a strength score using math
#save the result in file using os

# importing libraries
import random
import re
import math
import os
from collections import Counter

# 1. generate random password
length = 10
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()"

characters = letters + digits + symbols
password = "".join(random.choice(characters) for _ in range(length))

# 2. check password strength
strength = 0

if re.search(r"[a-z]", password):
    strength += 1
if re.search(r"[A-Z]", password):
    strength += 1
if re.search(r"\d", password):
    strength += 1
if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~\\-]", password):
    strength += 1
if len(password) >= 8:
    strength += 1

# 3. count characters used
char_count = Counter(password)

# 4. strength score using math
strength_score = math.ceil((strength / 5) * 100)

# strength label
if strength_score >= 80:
    level = "Strong"
elif strength_score >= 50:
    level = "Medium"
else:
    level = "Weak"

# 5. save result in file using os
if not os.path.exists("password_reports"):
    os.mkdir("password_reports")

file_path = os.path.join("password_reports", "password_report.txt")

with open(file_path, "w") as file:
    file.write(f"Generated Password: {password}\n")
    file.write(f"Strength Level: {level}\n")
    file.write(f"Strength Score: {strength_score}%\n")
    file.write("Character Count:\n")
    for char, count in char_count.items():
        file.write(f"{char} : {count}\n")

print("Password generated and report saved successfully.")
