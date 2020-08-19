s = "welcome to python"
print(s.isalnum())      #checks if string is alpha numeric
print(s.isalpha())      #checks if string has only alphabets
print(s.isdigit())      #checks if string has only digits
print(s.isidentifier()) #checks if a string is valid identifier
print(s.islower())      #checks is a string is in lowercase
print(s.isupper())      #cheks is a string in uppercase
print(s.isspace())      #checks if string contains only white spaces

print(s.endswith("thon"))    #checks if string ends with substring s1
print(s.startswith("hello")) #checks if string starts with substring s1
print(s.count("o"))          #returns number of time substring occured in  string
print(s.find("come"))        #returns lowest index where substring starts in a string
print(s.rfind("o"))          #returns highest index where substring starts in a string