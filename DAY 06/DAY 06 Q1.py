#re.match() Validation
import re

string1 = "EMP123"
result1 = re.match(r"EMP\d{3}", string1)
print(result1.group())

#re.search() for Email
text2 = "Contact us at support@company.com for help."
result2 = re.search(r"[\w.-]+@[\w.-]+\.[a-z]{2,}", text2)
print(result2.group())


#Meta-characters and Special Sequences
pattern3 = r"\d+\s\w+\s\?"
text3 = "123 apple ?"
result3 = re.search(pattern3, text3)
print(result3.group())


#Capturing Groups
text4 = "EMP456"
result4 = re.match(r"(EMP)(\d{3})", text4)
print(result4.group(1))
print(result4.group(2))

