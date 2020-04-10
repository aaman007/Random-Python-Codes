def square(n):
    return n*n


def multiply(a,b):
    return a*b

def greet(first,last):
    print(f'Hello, {first} {last}')


print("Hello")
print(square(7))
print(multiply(7,8))

# Positional Argument
greet("Aaman","Rahman")
greet("Rahman","Aaman")
# Keyword Argument
greet(last="Rahman",first="Aaman")  # We are telling which argument belongs to which parameter
# Combo
greet("Aaman",last="Rahman")  ## Always use the Keyword Arguments after the Positional Arguments



