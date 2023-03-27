# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name

# print(pet_names[0])

#3. ✅ Return all pet names beginning from the 3rd index
    # includes element with index of 3

# print(pet_names[3:])

#4. ✅ Return all pet names before the 3rd index
    # doesn't include element with index of 3

# print(pet_names[:3])

#5. ✅ Return all pet names beginning from the 3rd index and up to / including the 7th index

# print(pet_names[3:8])

#6. ✅ Find the index of a given element => .index()

# print(pet_names.index('Luke'))


#7. ✅ Reverse the original list => .reverse()

# pet_names.reverse()
# print(pet_names)

#8. ✅ Return the frequency of a given element => .count()

# print(pet_names.count("Luke"))

# Updating Lists
#9. ✅ Change the first pet_name to all uppercase letters => .upper()

# print(pet_names[0].upper()) 

#10. ✅ Append a new name to the list => .append()

# pet_names.append("Henry")
# print(pet_names)

#11. ✅ Add a new name at a specific index => .insert()

    #   .insert() is destructive
# pet_names.insert(2, "Joy")
# print(pet_names)

#12. ✅ Add two lists together => +

# print(pet_names + [4,5,6])

#13. ✅ Remove the final element from the list => .pop()

# pet_names.pop()
# print(pet_names)

#14. ✅ Remove element by specific index => .pop()

# pet_names.pop(1)
# print(pet_names)

#15. ✅ Remove a specific element => .remove()

# pet_names.remove("Rose")
# print(pet_names)

#16. ✅ Remove all pet names from the list => .clear()

# pet_names.clear()
# print(pet_names)

#Tuple
# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable
    
    # Why Are Tuples Immutable?

        # What advantages does this provide for us? In what situations
        # would this serve us?

#17. ✅ Create a Tuple of 10 pet ages => () 

pet_ages = (1,2,3,4,5,6,7,8,9,10,2)

#18. ✅ Print the first pet age => []

# print(pet_ages[0])

# Testing Mutability 
#19. ✅ Attempt to remove an element with ".pop" (should error)

# pet_ages.pop()

#20. ✅ Attempt to change the first element (should error) => []

# pet_ages[0] = 2

# Tuple Methods
#21. ✅ Return the frequency of a given element => .count()

# print(pet_ages.count(2))

#22. ✅ Return the index of a given element  => .index()

# print(pet_ages.index(10))

#23. ✅ Create a Range 
# Note:  Ranges are primarily used in loops
# my_range = range(60)
# for num in range(60):
#     print(num)

# Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}
# print(pet_fav_food)

# Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"

    # similar to a JSON object

pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}
# print(pet_info_rose)


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')
# print(pet_info_spot)

# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# print(pet_info_rose['temperament'])

#28. ✅ Print the pet attribute of "age" using ".get"

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error

# print(pet_info_spot.get('temperament', "Attribute not found!"))

# Updating 
#29. ✅ Update Rose's age to 12 => []

# pet_info_rose['age'] = 15
# print(pet_info_rose['age'])

#30. ✅ Update Spot's age to 26 => .update({...})

# pet_info_spot.update({'age': 26})
# print(pet_info_spot['age'])


# Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []

# del pet_info_rose['age']
# print(pet_info_rose)

#32. ✅ Delete Spot's age using ".pop"

# pet_info_spot.pop('age')
# print(pet_info_spot)


#33. ✅ Delete the last item for Rose using "popitem()"

# pet_info_rose.popitem()
# print(pet_info_rose)


# Loops 
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range

# range = range(10)
# for num in range:
#     print(num)

#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# new_range = range(50,60,2)
# for num in new_range:
#     print(num)


#36. ✅ Loop through the "pet_info" list and print every dictionary 

# for each_pet in pet_info:
#     print(each_pet)


#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument

# def ex_func(list):
#     for item in list:
#         print(item)

# ex_func(pet_names)


#38. ✅ Create a function that takes a list as a parameter
    # The function should define a variable ("counter") and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Once the loop has finished, return the final value of "counter"

# def counter_func(list):
#     counter = 0
#     while counter < len(list):
#         counter += 1
#     return counter

# print(counter_func(pet_info))

#39. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'

# def update_pet_age(list, name, age):
#     index = 0
#     while(list[index]['name'] != name and index < len(list) - 1):
#         index += 1
#     if (list[index]['name'] == name):
#         list[index]['age'] = age
#         return list
#     else:
#         return 'Pet not found'

# print(update_pet_age(pet_info, "Rose", 12))


# map like 
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase

# upper_pet_names = [ animal_name.upper() for animal_name in pet_info['name']]

# print(pet_info)
# new_pet_list = [pet.get('name').upper() for pet in pet_info]
# print(new_pet_list)
# print(pet_info)

# find like
#41. ✅ Use list comprehension to find a pet named spot

# find_spot = [pet for pet in pet_info if pet.get('name') == "Spot"]
# print(find_spot)

# filter like
#42. ✅ Use list comprehension to find all of the pets under 3 years old

# filter_age = [pet for pet in pet_info if pet.get('age') < 3]
# print(len(filter_age))
# print(filter_age)

#43. ✅ Create a generator expression matching the filter above

# Main Benefit => Less memory intensive

young_pets = (pet for pet in pet_info if pet.get("age") < 26)

# print(next(young_pets))
# print(next(young_pets))
# print(next(young_pets))

for pet in young_pets:
    print(pet)
