# A... String Operation
# Reverse the given string 
print("A...")
mystr = input("Enter String : ")
print("\nReverese String of ", mystr , " is : ", mystr[::-1])

# Replace some character of the string with another character
modified_str = mystr.replace('R' , 'r')
print("\nOriginal String : ", mystr, "\nModified String : " , modified_str)

# Merge two string
mystr1 = "Hello"
merged_str = mystr1 + " " + mystr
print("\nMerged String : ", merged_str)

# Find whether the character in the given string or not.
if('o' in mystr) :
    print("\nCharacter 'o' is presant in given string ", mystr)
else :
    print("\nCharacter 'o' is not presant in given string ", mystr)
    
# Split String 
mystr2 = "Hello, Hii, Whats'app"
splited_str = mystr2.split(',')
print("\nSplit String with ',' : ", splited_str)



# B... Dictonary Operation
print("\nB...")
student = {
    'name' : 'Rutik Dobariya',
    'age' : 19,
    'grade' : 'A+'
}
print("My student Dictionary : ")
for key,val in student.items() :
    print(f"{key} : {val}")
    
# Update a value
student['age'] = 20
print("\nDictionary after Update Age : ", student)

# Delete a value
del student['grade']
print("Dictionary after Delete Grade : ", student)

# Clear Dictionary
student.clear()
print("Dictionary after Clearing : ", student)

# Defing student Dictionary 
student = {
    'name' : 'Rutik Dobariya',
    'age' : 19,
    'grade' : 'A+'
}
print("\nDefining My student Dictionary : ")
for key,val in student.items() :
    print(f"{key} : {val}")
    
# Remove and return a (key, value) pair as a 2-tuple
removed_item = student.popitem()
print("\nRemoved item:", removed_item)
print("Dictionary after popitem:", student)

# Remove a key and return its value
age = student.pop('age')
print("\nRemoved age:", age)
print("Dictionary after pop('age'):", student)

# Add element in dictionary
student['year'] = 2
student['sem'] = 4

# Get a value for a given key, returns None if key not present
name = student.get('name')
print("\nValue of 'name':", name)

# Get all keys in the dictionary
keys = student.keys()
print("\nKeys:", keys)

# Get all values in the dictionary
values = student.values()
print("\nValues:", values)

# Create 3 dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Merge dictionaries into one
merged_dict = {**dict1, **dict2, **dict3}
print("\nMerged dictionary:", merged_dict)