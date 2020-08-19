import re

str1 = "Welc0me@!@#toPython)**^%(Programming"

regex=re.compile('[~!@#$%^&*<>?:]')

if(regex.search(str) == None):
    print("No Special characters present in the string")
else:
    print("String contains special characters")