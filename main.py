def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mult(a, b):
    return a * b

def dev(a, b):
    if(b != 0):
        return a / b

print("Welcome to my calculator!")

a = input("Enter a number: ")
b = input("Enter another number: ")

a = int(a)
b = int(b)

print(add(a, b))

