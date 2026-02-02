##
import re

#1. (.)
text = "cat cot cut"
result = re.findall("c.t",text)
print(result)

#2. starting of a string(^)
text = "Hello World"
print(bool(re.search("^Hello",text)))
print(bool(re.search("^World",text)))

#3. ending of a string($)
text = "Hello World"
print(bool(re.search("World$",text)))
print(bool(re.search("Hello$",text)))

#4. zero or more(*)
text = "helloooo"
result = re.findall("lo*",text)
print(result)

#5. one or more(+)
text = "helloooo"
result = re.findall("lo+",text)
print(result)

#6. 0 or 1 time(?)
text = "color colour"
result = re.findall("colou?r",text)
print(result)

#7. character set([])
text = "apple ball cat"
result = re.findall("[abc]",text)
print(result)

#8. Digits([0-9])
text = "my age is 90"
result = re.findall("[0-9]",text)
print(result)

#9.Capital Letters([A-Z])
text = "my age is 90"
result = re.findall("[A-Z]",text)
print(result)

#10. Small Letters[a-z]
text = "my age is 90"
result = re.findall("[a-z]",text)
print(result)

#11. All letters[A-Za-Z]
text = "my age is 90"
result = re.findall("[A-Za-z]",text)
print(result)

#12. Digits (\d)
text = "Marks: 90"
result = re.findall(r"\d",text)
print(result)

#13. Non Digits(\D)
text = "Marks: 90"
result = re.findall(r"\D",text)
print(result)

#14. Word Character(\w)
text = "Marks: 90"
result = re.findall(r"\w",text)
print(result)

#15. not word character(\W)
text = "Marks: 90"
result = re.findall(r"\W",text)
print(result)

#16. space (\s)
text = "Marks: 90"
result = re.findall(r"\s",text)
print(result)

#17. No space(\S)
text = "Marks: 90"
result = re.findall(r"\S",text)
print(result)

#18.repetition count({})
text = "Phone: 873939123427"
result = re.findall(r"\d{10}",text)
print(result)

#19. or operator(|)
text = "I have a cat and a dog"
result = re.findall(r"cat|dog",text)
print(result)

#20. grouping()
text = "abab ab"
result = re.findall("(ab)+",text)
print(result)










































