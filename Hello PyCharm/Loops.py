# Loops
# For Loop Syntax
for i in range(5): # i = 0,1,2,3,4
    print(i)
for i in range(1,5): # i = 1,2,3,4
    print(i)


# Iterating over Lists or Strings
for item in "Aaman":
    print(item)
for item in ["Aaman" , "Rahman" , "Amanur"]:
    print(item)


# While Loop Syntax
condition = True
while condition:
    print()
    a = int(input())
    if a == 10:
        break  # similarly we can use continue
print('Done')


# While loops has an optional else part
n = 5
i = 0
while(i < n):
    i = i+1
    a = int(input())
    if a == 99:
        print('Great')
        break
    else:
        continue
else: # executes if while loop completes successfully without any immediate breaks
    print('Sad')


# Exercise
numbers = [5,2,5,2,2] # lists
for item in numbers:
    line = ""
    for x in range(item):
        line += "X"
    print(line)

