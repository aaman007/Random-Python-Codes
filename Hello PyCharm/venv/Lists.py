# Lists

names = ["Aaman","Rahman","Amanur","Sunny"]
print(names)
print(names[1])  # Rahman
print(names[1:]) # returns list from index 1
print(names[1:3]) # return list with index 0,1
print(names[-1]) # first element from last


# Exercise
numbers = [1,2,1,10,5,20,11,15]
mx = 0
for i in numbers:
    mx = max(mx,i)
print(i)


# 2D Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print(matrix[1])
print(matrix[0][2])
for row in matrix:
    for item in row:
        print(item)


# List Methods
numbers = [1,5,5,2,3]
numbers.append(10)  # adds element 10 at the end of list
print(numbers)
numbers.insert(0,20)  # adds element 20 at 0th index
print(numbers)
numbers.remove(2) # removes 2 from the list
print(numbers)
numbers.pop() # removes last item of list
print(numbers)
if 20 in numbers:
    print(numbers.index(20)) # returns index of first occurrence of 20 in the list
print(numbers.count(5)) # returns number of occurrences of 5 in the list
numbers.sort()  # sorts the list in ascending order
print(numbers)
numbers.reverse()  # reverses the list
print(numbers)
numbers2 = numbers.copy()  # copies number list to number2 list
numbers.clear() # removes all the items of the list
print(numbers)



# Exercise
list = [1,2,2,5,3,5]
unique = []
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)


# Split string into lists
message = "Hello, what are you doing?"
words = message.split(' ')  # Splits string wherever it find space
print(words)