# !/usr/bin/env python3
    # Defines the location of the Python interpreter
    # See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes

# 1. ✅ Create a Pet class

class Pet:

# 2. ✅ Instantiate a few Pet instances

    # Compare the Pet instances. Are each of them the same object?

        # not the same object
        # created from the same class

# 3. ✅ Demonstrate __init__ 

    # Add arguments to instances  

    # Attributes:
        # name
        # age
        # breed
        # temperament
        # owner

    def __init__(self, name, age, breed, temperament, owner = "No Owner"):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.owner = owner
    
    # Use dot notation to access each Pet instance's attributes 

    # Update attributes with new values

# Instance Methods

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's 
# attributes

    # Review the "self" keyword 
    
    # Invoke "print_pet_details" on an instance 
    def print_pet_details(self):
        print(f'''
            name: {self.name}
            age: {self.age}
            breed: {self.breed}
            temperament: {self.temperament}
        ''')
    
    # Example Terminal Ouput:
        # name: Rose
        # age: 11
        # breed: Domestic Longhair
        # temperament: Sweet

# 5. ✅ Create an Owner class with two instance methods:

class Owner:
    def __init__(self, age):
        self.age = age

    # get_name => Retrieve Owner's name
    def get_name(self):
        return self._name
    
    # set_name => Set Owner's name
    def set_name(self, name):
        if type(name) == str:
            self._name = name
        else:
            print("Name must be a string")

        # Ensure that Owner's name is a String

        # If not, issue warning of "Name must be a string"
    
    name = property(get_name, set_name)

    # Use property() to compile get_name / set_name and invoke them
    # whenever we access an Owner instance's name

    # Object Properties => Attributes that are controlled by methods

    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if type(age) == int and (21 <= age <= 50):
            self._age = age
        else:
            print("Please use a number between 21 and 50.")
    age = property(get_age, set_age)