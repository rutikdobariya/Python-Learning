# A...
print("A...")
mylist = ['Rutik',0,5,'Dharmik',12,'Pujan']

# Append()
mylist.append(20)
mylist.append('Jash')

print("My list : ", mylist)

# extend()
mylist1 = ['Apple', 56, 10]
mylist.extend(mylist1)

print("My list after extending another list : ", mylist)

# remove()
mylist.remove("Apple")
mylist.remove(56)
print("My list after Remove elements : ", mylist)

# reverse()
mylist.reverse()
print("My list after Reverse the list : ", mylist)

# arrange in ascending order
mylist2 = [52,69,42,35,9,0,54,10]
mylist2.sort()
print("My list after arrange element in ascending ordere : ", mylist2)

# arrange in ascending order
mylist2 = [52,69,42,35,9,0,54,10]
mylist2.sort(reverse=True)
print("My list after arrange element in descending ordere : ", mylist2)



# B...
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]
orange = List1[-1][-1]
python = List1[4][0]
print("\nB...")
print("Element 'Orange' : ", orange)
print("Element 'Python' : ", python)

# Repeat this list 
newlist = [List1] * 5
print("Repeated List :\n", newlist)



# C...
print("\nC...")
copylist = mylist[0::]
print("Copied List : ", copylist)



# D...
print("\nD...")
mytuple = (52,63,0,25,1,29)

# sum()
print("Sum :", sum(mytuple)) # Sum : 170

# max()
print("Maximum :", max(mytuple)) # Maximum : 63

# min()
print("Minimum :", min(mytuple)) # Minimum : 0

# len()
print("Length :", len(mytuple)) # Length : 6

# Average
print("Average :", sum(mytuple) / len(mytuple)) # Average : 28.333333333333332