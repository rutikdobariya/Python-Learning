# 1... Create an empty tuple
tuple1 = ()

# 2... Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Jenil','Sarthak','Jainesh','Dharmik','Jash','Pujan')
sisters = ('Nishtha','Hasti','Devangi','Krisha','Swati')

# 3... Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters # ('Jenil', 'Sarthak', 'Jainesh', 'Dharmik', 'Jash', 'Pujan', 'Nishtha', 'Hasti', 'Devangi', 'Krisha', 'Swati')

# 4... How many siblings do you have?
print("Number of My Siblings  = ", len(siblings)) # Number of My Siblings  =  11

# 5... Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Mukeshbhai','Ranjanben') # ('Jenil', 'Sarthak', 'Jainesh', 'Dharmik', 'Jash', 'Pujan', 'Nishtha', 'Hasti', 'Devangi', 'Krisha', 'Swati', 'Mukeshbhai', 'Ranjanben')

# 6... Unpack siblings and parents from family_members
*siblings,father,mother = family_members
print("Siblings = ", siblings) # Siblings =  ['Jenil', 'Sarthak', 'Jainesh', 'Dharmik', 'Jash', 'Pujan', 'Nishtha', 'Hasti', 'Devangi', 'Krisha', 'Swati']
print("Father = ", father) # Father =  Mukeshbhai
print("Mother = ", mother) # Mother =  Ranjanben

# 7... Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Orange", "KiWi", "Mango", "Lichi", "Apple", "Cherry")
vegetables = ("Cabbage", "Brinjal", "Carrot","Potato", "Tomato")
animal_products = ("Eggs", "Milk", "Cheese", "Meat", "Honey")
food_stuff_tp = fruits + vegetables + animal_products # ('Orange', 'KiWi', 'Mango', 'Lichi', 'Apple', 'Mango', 'Cabbage', 'Brinjal', 'Carrot', 'Potato', 'Tomato', 'Eggs', 'Milk', 'Cheese', 'Meat', 'Honey')

# 8... Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp) # ['Orange', 'KiWi', 'Mango', 'Lichi', 'Apple', 'Mango', 'Cabbage', 'Brinjal', 'Carrot', 'Potato', 'Tomato', 'Eggs', 'Milk', 'Cheese', 'Meat', 'Honey']

# 9... Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = float(len(food_stuff_lt))/2
if len(food_stuff_lt) % 2 != 0:
    # print(middle)
    print("Median food_stuff_lt = " ,food_stuff_lt[int(middle - .5) : (int(middle - .5) + 1)])
else:
    print ("\nMedian food_stuff_lt = " ,food_stuff_lt[int(middle-1) : int(middle+1)])
# Median food_stuff_lt =  ['Brinjal', 'Carrot']

# 10... Slice out the first three items and the last three items from food_staff_lt list
print("first three items from food_staff_lt list : ", food_stuff_lt[:3]) # first three items from food_staff_lt list :  ['Orange', 'KiWi', 'Mango']
print("last three items from food_staff_lt list : ", food_stuff_lt[-3:]) # last three items from food_staff_lt list :  ['Cheese', 'Meat', 'Honey']

# 11... Delete the food_staff_tp tuple completely
del food_stuff_tp

# 12... Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Check if 'Estonia' is a nordic country = ", 'Estonia' in nordic_countries) # Check if 'Estonia' is a nordic country =  False

# 13... Check if 'Iceland' is a nordic country
print("Check if 'Iceland' is a nordic country = ", 'Iceland' in nordic_countries) # Check if 'Iceland' is a nordic country =  True