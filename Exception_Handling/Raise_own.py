#To raise an exception on your own, we need to use raise keyword

def EnterAge(age):
    if age <= 0:
        raise ValueError("only positive integers are allowed - age must be more than zero")

    if age % 2 == 0:
        print("Even age")

    else:
        print("Odd age")

num=0
EnterAge(num)



