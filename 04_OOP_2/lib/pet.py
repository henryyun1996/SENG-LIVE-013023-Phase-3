#!/usr/bin/env python3
# Class Attributes and Methods 

import ipdb

class Pet:

# 4. ✅ Define a class attribute (total_pets) and set it to 0

    # Class Attribute

    total_pets = 0

    # What happens with our instances when we add a class attribute?

    def __init__(self,name, age, breed, temperament):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament

# 5. ✅. Update the class attribute whenever an instance is initialized

        # Pet.total_pets += 1
        Pet.increase_pets()

# 6. ✅. Create a class method increase_pets that will increment total_pets
    
    # replace Pet.total_pets += 1 in __init__ with Pet.increase_pets()

    # Instance Method
    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')

    # Class Method
    @classmethod
    def increase_pets(cls):
        cls.total_pets += 1
        print("One new pet added")