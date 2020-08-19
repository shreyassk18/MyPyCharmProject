string="Welcome to python programming"

words=string.split(" ") #This will split a string on white spaces
print(words)

words=(words[-1::-1])
print(words)

output=' '.join(words)   #This will convert list entris to a string
print(output)