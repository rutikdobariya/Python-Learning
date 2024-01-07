# 1... Create  an empty dictionary called dog
dog = {}

# 2... Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Collie',
    'color': 'Blue Merle',
    'breed': 'Border Collie',
    'legs': 4,
    'age': 7
} # {'name': 'Collie', 'color': 'Blue Merle', 'breed': 'Border Collie', 'legs': 4, 'age': 7}

# 3... Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Rutik',
    'last_name': 'Dobariya',
    'gender' : 'Male',
    'age': 19,
    'is_marred': False,
    'skills': ['Kabbadi','Cricket','Laravel','Badminton','Sql'],
    'country': 'India',
    'city' : 'Surat',
    'address':{
        'street':'Kathodara',
        'pincode':'394326'
    }
    } # {'first_name': 'Rutik', 'last_name': 'Dobariya', 'gender': 'Male', 'age': 19, 'is_marred': False, 'skills': ['Kabbadi', 'Cricket', 'Laravel', 'Badminton', 'Sql'], 'country': 'India', 'city': 'Surat', 'address': {'street': 'Kathodara', 'pincode': '394326'}}

# 4... Get the length of the student dictionary
print("Length of Student Directory is : ", len(student)) # Length of Student Directory is :  9

# 5... Get the value of skills and check the data type, it should be a list
print(type(student['skills'])) # <class 'list'>
print('Skills are :')
for val in student['skills']:
    print(val)
    # Skills are :
    # Kabbadi
    # Cricket
    # Laravel
    # Badminton
    # Sql

# 6... Modify the skills values by adding one or two skills
student['skills'].append('Table Tennis')
print('Skills are :')
for val in student['skills']:
    print(val)
    # Skills are :
    # Kabbadi
    # Cricket
    # Laravel
    # Badminton
    # Sql
    # Table Tennis
    
# 7... Get the dictionary keys as a list
print('Student Dictionary keys are : ', student.keys()) # Student Dictionary keys are :  dict_keys(['first_name', 'last_name', 'gender', 'age', 'is_marred', 'skills', 'country', 'city', 'address'])

# 8... Get the dictionary values as a list
print('Student Dictionary values are : ', student.values()) # Student Dictionary values are :  dict_values(['Rutik', 'Dobariya', 'Male', 19, False, ['Kabbadi', 'Cricket', 'Laravel', 'Badminton', 'Sql', 'Table Tennis'], 'India', 'Surat', {'street': 'Kathodara', 'pincode': '394326'}])

# 9... Change the dictionary to a list of tuples using _items()_ method
student_tuple = student.items() # dict_items([('first_name', 'Rutik'), ('last_name', 'Dobariya'), ('gender', 'Male'), ('age', 19), ('is_marred', False), ('skills', ['Kabbadi', 'Cricket', 'Laravel', 'Badminton', 'Sql', 'Table Tennis']), ('country', 'India'), ('city', 'Surat'), ('address', {'street': 'Kathodara', 'pincode': '394326'})])

# 10... Delete one of the items in the dictionary
student.pop('city')
for key, val in student.items():
    print(f"{key} : {val}")
    
    # first_name : Rutik
    # last_name : Dobariya
    # gender : Male
    # age : 19
    # is_marred : False
    # skills : ['Kabbadi', 'Cricket', 'Laravel', 'Badminton', 'Sql', 'Table Tennis']
    # country : India
    # address : {'street': 'Kathodara', 'pincode': '394326'}
    
# 11... Delete one of the dictionaries
del dog
print(dog) # NameError: name 'dog' is not defined