# Multi-line string
ML_message = '''Hello Aaman,
This is John Doe
Good Bye'''
print(ML_message)


# Formatted Strings
first = 'Amanur'
last = 'Rahman'
# text0 = first + ' [' + last + ']' + ' loves programming' # Not Readable for all
# print(text0)
text = f'{first} [{last}] loves programming'
print(text)


# Substrings
name = 'Amanur Rahman'
print(name[2:]) # anur Rahman
print(name[:4]) # Aman
print(name[:]) # Amanur Rahman
print(name[1:-1]) # manur Rahma # -1 indicates first character from last


# String Methods
name = 'Amanur Rahman'
print(len(name))  # returns length of string , but this is a general purpose function, not a string method


print(name.upper()) # returns all letter in uppercase , this is a string method
print(name.lower())
print(name.find('a'))  # returns index of first occurrence of 'a' in string , returns -1 in case there is no such letter
print(name.find('Rah')) # returns index of first occurrence of substring (index where it starts)
print(name.replace('Amanur','Aaman')) # replaces all occurrences substring with second argument
print(name.replace('a','A'))  # replaces letter
print('Aman' in name)  # returns True as Aman does occurs in string
