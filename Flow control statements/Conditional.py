#Example 1
a=10
if a>5:
    print("True condition")
else:
    print("False condition")

#Example 2
if True:
    print("True condition")
else:
    print("Flase condition")

#Example 3
if 1:
    print("True Condition")
else:
    print("False condition")

#Example 4 (even or odd)
if a % 2 == 0:
    print("True condition")
else:
    print("False condition")

#Multiple statement in conditions
if True:
    print("Statement1")
    print("Statement2")
else:
    print("Statement3")
    print("Statement4")

#Single statement in single line
print("welcome") if True else print("python")
print("welcome") if 10<20 else print("python")

#Multiple statementments in single line
#We have to enclose multiple statements in curly braces
{print("welcome1"),print("python1")} if True else {print("welcome2"), print("python2")}

#elif condition
a=10
if a == 10:
    print("ten")
elif a == 20:
    print("twenty")
elif a == 30:
    print("thirty")
else:   #optional
    print("Not applicable")