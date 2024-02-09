# 1... Reverse the given string (You can take any string)
my_str = input("Enter String : ")
print("\nReverese String of ", my_str , " is : ", my_str[::-1])

# 2... Replace some character of the string with another character without using a loop.
modified_str = my_str.replace('R' , 'r')
print("\nOriginal String : ", my_str, "\nModified String : " , modified_str)

# 3... Find whether the character in the given string or not.
if('o' in my_str) :
    print("\nCharacter 'o' is presant in given string ", my_str)
else :
    print("\nCharacter 'o' is not presant in given string ", my_str)

# 4... Create tuple, list and set and convert them into the different strings.

# Create a tuple
my_tuple = (1, 2, "Tuple", 4, 'A')

# Convert tuple to string
tuple_string = str(my_tuple)

# Create a list
my_list = [1, 2, "List", 4, 'B']

# Convert list to string
list_string = str(my_list)

# Create a set
my_set = {1, 2, "Set", 4, 'C'}

# Convert set to string
set_string = str(my_set)

# Print the string representations
print("\nTuple as string:", tuple_string)
print("List as string:", list_string)
print("Set as string:", set_string)

# 5... Convert all the string characters to the upper and the lower case and split it with the different methods.
print("\nConvert string to Upper Case : ", my_str.upper())
print("Convert string to Lower Case : ", my_str.lower())

splited_str = my_str.split(',')
print("\nSplit String with ',' : ", splited_str)

# 6... Perform the following operations to the tuple and the list
# 	Find max, min, len, sum
my_tuple1 = (62,2,0,36,45,96,9)
my_list1 = [65,23,45,0,32,25,98,12]

print("\nTuple :")
print("My Tuple : ", my_tuple1)
print("Max : ", max(my_tuple1))
print("Min : ", min(my_tuple1))
print("Length : ", len(my_tuple1))
print("Sum : ", sum(my_tuple1))

print("\nList :")
print("My List : ", my_list1)
print("Max : ", max(my_list1))
print("Min : ", min(my_list1))
print("Length : ", len(my_list1))
print("Sum : ", sum(my_list1))

# 7... Copy one list to the another list without using the copy command.
copied_list = my_list[:]

print("\nCopied list :", copied_list)

# 8... Create a dictionary named student with keys: 'name', 'age', and 'grade'. Assign 	values accordingly.
student = {
    'name' : 'Rutik Dobariya',
    'age' : 19,
    'grade' : 'A+'
}
print("\nMy student Dictionary : ")
for key,val in student.items() :
    print(f"{key} : {val}")
    
# Print the 'age' of the student from the dictionary created in Exercise 1.
print('\nAge of Student : ', student['age'])

# Update the 'grade' of the student to a new value.
student['grade'] = 'A++'
print('\nUpdated Grade of Student : ', student['grade'])

# 9... Set Creation 
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of set
print('\nUnion of set1 and set2 : ', set1|set2)

# Intersection of set
print('Intersection of set1 and set2 :', set1.intersection(set2))

# elements that are in set1 but not in set2
print('Elements that are in set1 but not in set2 : ', set1 - set2)

# Check if set1 is a subset of set2
if set1.issubset(set2):
    print("set1 is a subset of set2.")
else:
    print("set1 is not a subset of set2.")


# 10... Create a dictionary where keys are subjects and values are sets of students
subjects_students = {
    'math': {'Dharmik', 'Jash', 'Pujan',},
    'science': {'Jenil', 'Vishnu', 'Hansil', 'Sanket', 'Dharmik'}
}

print("\nMy Student Dictionary : ")
for subject, students in subjects_students.items():
    print(f"Subject: {subject}")
    print("Students:", students)

# Add a new student to the 'math' subject
subjects_students['math'].add('Arshil')
print("\nAdded new student to math subject : ", subjects_students["math"])

# Remove a student from the 'science' subject
subjects_students['science'].remove('Sanket')
print("\nRemove one student from science subject : ", subjects_students["science"])

# Find and print the students who take both 'math' and 'science'
common_students = subjects_students['math'].intersection(subjects_students['science'])
print("\nCommon students:", common_students, '\n')

# Create a nested dictionary with countries, cities, and populations
population_data = {
    'India': {'Mumbai': 12442373, 'Delhi': 11034555, 'Banglore': 8443675, 'Ahemdabad' : 5577940, 'Chennai' : 4646732},
    'Canada': {'Toronto': 2600000, 'Montreal': 1600000, 'Calgary': 1019942, 'Ottawa' : 812129},
    'Australia' : {'Sydney' : 5297089, 'Melbourne' : 5031195, 'Brisbane' : 2628083, 'Perth' : 2224475, 'Adelaide' : 1418455, 'ACT' : 456692}
}
# Print the nested dictionary
for country, cities in population_data.items():
    print(f"Country: {country}")
    for city, population in cities.items():
        print(f"    City: {city}, Population: {population}")
              
# 11... Create two lists, one containing elements at even indices and the other containing elements at odd indices from the original list.
# Original list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List containing elements at even indices
even_indices_list = original_list[::2]

# List containing elements at odd indices
odd_indices_list = original_list[1::2]

# Print the resulting lists
print("\nElements at even indices:", even_indices_list)
print("Elements at odd indices:", odd_indices_list)

# 12... Use tuple packing and unpacking to swap the values of two variables without using a temporary variable.
a = 5
b = 10

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swap the values using tuple packing and unpacking
a, b = b, a

# Print the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)

# Check if a given list is a palindrome using slicing.
my_list2 = [1, 2, 3, 2, 1]

# 13... Check if the list is a palindrome using slicing
is_palindrome = my_list2 == my_list2[::-1]

# Print the result
if is_palindrome:
    print("\nThe list is a palindrome.")
else:
    print("\nThe list is not a palindrome.")

# 14... catenate two tuples without using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenate the two tuples without using the + operator
concatenated_tuple = (*tuple1, *tuple2)

# Print the concatenated tuple
print("\nConcatenated tuple:", concatenated_tuple)
