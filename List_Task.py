# 1... Declare an empty list
list1 = list() # Declare an empty list

# 2... Declare a list with more than 5 items
list2 = ["Rutik","Dobariya","D23CE152",1,2,'A','b'] # Declare a list with more than 5 items

# 3... Find the length of your list
print("Lenght of list2 = " ,len(list2)) # Lenght of list2 =  7

# 4... Get the first item, the middle item and the last item of the list
middle = float(len(list2))/2
if int(len(list2)) % 2 != 0:
    print("First iteam in list2 = " ,list2[0], "\nMiddle iteam in list2 = " ,list2[int(middle - .5)], "\nLast iteam in list2 = " ,list2[-1])
else:
    print("First iteam in list2 = " ,list2[0], "\nMiddle iteams in list2 = " ,list2[int(middle-1)], " AND " ,list2[int(middle)], "\nLast iteam in list2 = " ,list2[-1])
    # First iteam in list2 =  Rutik 
    # Middle iteam in list2 =  1 
    # Last iteam in list2 =  b 
    
# 5... Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Rutik Dobariya",19,6,"unmarried","94, Santiniketan Society, Kathodara, Surat"] # List with Mixed Data TYpe

# 6... Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"] # List of It Compnies

# 7... Print the list using _print()_
print("mixed_data_types List = ", mixed_data_types, "\nit_companies list = ", it_companies) # mixed_data_types List =  ['Rutik Dobariya', 19, 6, 'unmarried', '94, Santiniketan Society, Kathodara, Surat'] 
                                                                                            # it_companies list =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 8... Print the number of companies in the list
print("Number of companies in it_companies List = ", len(it_companies)) # Number of companies in it_companies List =  7

# 9... Print the first, middle and last company
middle = float(len(it_companies))/2
if int(len(it_companies)) % 2 != 0:
    print("First company in list2 = " ,it_companies[0], "\nMiddle company in list2 = " ,it_companies[int(middle - .5)], "\nLast company in list2 = " ,it_companies[-1])
else:
    print("First company in list2 = " ,it_companies[0], "\nMiddle companies in list2 = " ,it_companies[int(middle-1)], " AND " ,it_companies[int(middle)], "\nLast company in list2 = " ,it_companies[-1])
    # First company in list2 =  Facebook 
    # Middle company in list2 =  Apple 
    # Last company in list2 =  Amazon

# 10... Print the list after modifying one of the companies
it_companies.insert(5,'InfoSystem')  # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'InfoSystem', 'Oracle', 'Amazon']
# print(it_companies)

# 11... Add an IT company to it_companies
it_companies.append("TCS") # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'InfoSystem', 'Oracle', 'Amazon', 'TCS']
# print(it_companies)

# 12... Insert an IT company in the middle of the companies list
middle = float(len(it_companies))/2
it_companies.insert(int(middle), "Wipro") # ['Facebook', 'Google', 'Microsoft', 'Apple', 'Wipro', 'IBM', 'InfoSystem', 'Oracle', 'Amazon', 'TCS']
# print(it_companies)

# 13... Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[int(middle)] = it_companies[int(middle)].upper() # ['Facebook', 'Google', 'Microsoft', 'Apple', 'WIPRO', 'IBM', 'InfoSystem', 'Oracle', 'Amazon', 'TCS']
# print(it_companies)

# 14... Join the it_companies with a string '#;&nbsp; '
it_companies_string = '#;\n'.join(it_companies)
# print(it_companies_string)
    # Facebook#;
    # Google#;
    # Microsoft#;
    # Apple#;
    # WIPRO#;
    # IBM#;
    # InfoSystem#;
    # Oracle#;
    # Amazon#;
    # TCS

# 15... Check if a certain company exists in the it_companies list.
print("Checks for Wipro in it_companies list = ", 'Wipro' in it_companies) # Checks for Wipro in it_companies list =  False
print("Checks for WIPRO in it_companies list = ", 'WIPRO' in it_companies) # Checks for WIPRO in it_companies list =  True

# 16... Sort the list using sort() method
it_companies.sort() # Sorted list =  ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'InfoSystem', 'Microsoft', 'Oracle', 'TCS', 'WIPRO']
# print("Sorted list = ",it_companies)

# 17... Reverse the list in descending order using reverse() method
it_companies.reverse() # Sorted list in descending order =  ['WIPRO', 'TCS', 'Oracle', 'Microsoft', 'InfoSystem', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']
# print("Sorted list in descending order = ",it_companies) 

# 18... Slice out the first 3 companies from the list
print("Slice out the first 3 companies from the list : ", it_companies[0:3]) # Slice out the first 3 companies from the list :  ['WIPRO', 'TCS', 'Oracle']

# 19... Slice out the last 3 companies from the list
print("Slice out the last 3 companies from the list : ", it_companies[-3:]) # Slice out the last 3 companies from the list :  ['Facebook', 'Apple', 'Amazon']

# 20... Slice out the middle IT company or companies from the list
middle = float(len(it_companies))/2
if int(len(it_companies)) % 2 != 0:
    print("Middle company in list2 = " ,it_companies[int(middle - .5) : (int(middle - .5) + 1)])
else:
    print ("\nMiddle companies in list2 = " ,it_companies[int(middle-1) : int(middle+1)])
    # Middle companies in list2 =  ['InfoSystem', 'IBM']

# 21... Remove the first IT company from the list
it_companies.pop(0) # ['TCS', 'Oracle', 'Microsoft', 'InfoSystem', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']
# print(it_companies)

# 22... Remove the middle IT company or companies from the list
middle = float(len(it_companies))/2
if int(len(it_companies)) % 2 != 0:
    it_companies.pop(int(middle - .5))
else:
    it_companies.pop(int(middle))
    it_companies.pop(int(middle-1))
# print(it_companies)
    # ['TCS', 'Oracle', 'Microsoft', 'InfoSystem', 'Google', 'Facebook', 'Apple', 'Amazon']

# 23... Remove the last IT company from the list
it_companies.pop(-1) # ['TCS', 'Oracle', 'Microsoft', 'InfoSystem', 'Google', 'Facebook', 'Apple']
# print(it_companies)

# 24... Remove all IT companies from the list
it_companies.clear() # []
# print(it_companies)

# 25... Destroy the IT companies list
del it_companies # Destroying the IT companies list

# 26... Join the List
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
language = front_end + back_end # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
# print(language)

# 27... After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = language.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL') # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']
# print(full_stack)

# 28... Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
max_val = ages[-1]
min_val = ages[0]
print("Min age = ", min_val, ", Max age = ", max_val) # Min age =  19 , Max age =  26

# 29... Add the min age and the max age again to the list
ages.append(max_val)
ages.append(min_val) # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]

# 30... Find the median age (one middle item or two middle items divided by two)
ages.sort()
middle = float(len(ages))/2
if len(ages) % 2 != 0:
    # print(middle)
    print("median age = " ,ages[int(middle - .5) : (int(middle - .5) + 1)])
else:
    print ("\nmedian ages = " ,ages[int(middle-1) : int(middle+1)])
# median ages =  [24, 24]

# 31... Find the average age (sum of all items divided by their number )
print("Average Age is : ", sum(ages)/len(ages)) # Average Age is :  22.75

# 32... Find the range of the ages (max minus min)
print("Range of the ages : ", round(max(ages) - min(ages)))
# print(ages)

# 33... Compare the value of (min - average) and (max - average), use _abs()_ method
min_avg_diff = abs(min(ages) - (sum(ages)/len(ages)))
max_avg_diff = abs(max(ages) - (sum(ages)/len(ages)))
print("min - average = ", min_avg_diff) # min - average =  3.75
print("max - average = ", max_avg_diff) # max - average =  3.25
if min_avg_diff < max_avg_diff :
    print("(min - average) < (max - average)")
elif min_avg_diff > max_avg_diff :
    print("(min - average) > (max - average)")
else :
    print("(min - average) = (max - average)")
    # (min - average) > (max - average)
    
# 34... Find the middle country(ies) in the [countries list]
contries = ['India','Canada','Australia','U.K.','China','Netherland']
middle = float(len(contries))/2
if len(contries) % 2 != 0:
    print("Median contry = " ,contries[int(middle - .5) : (int(middle - .5) + 1)])
else:
    print ("\nMedian contries = " ,contries[int(middle-1) : int(middle+1)])
# Median contries =  ['Australia', 'U.K.']
    
# 35... Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(contries) % 2 != 0:
    middle = int(middle - .5)
    first_half = contries[:(middle + 1)]
    second_half = contries[(middle + 1):]
else:
    first_half = contries[:int(middle)]
    second_half = contries[int(middle):]
print("First half of Contries : ", first_half) # First half of Contries :  ['India', 'Canada', 'Australia']
print("Second half of Contries : ", second_half) # Second half of Contries :  ['U.K.', 'China', 'Netherland']

# 36...  Unpack the first three countries and the rest as scandic countries.
contries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_half2 = contries2[:3]
scandic_contries = contries2[3:]
print("First half of Contries : ", first_half2) # First half of Contries :  ['China', 'Russia', 'USA']
print("Scandic Contries : ", scandic_contries) # Scandic Contries :  ['Finland', 'Sweden', 'Norway', 'Denmark']