import ipdb

# 7. ✅. Create a subclass of Pet called Cat
    
    # import Pet from lib.pet

from lib.pet import Pet

class Cat(Pet):


# 8. ✅. Create Cat class + __init__ that takes all the parameters from Pet and an
# additional parameter called indoor (Boolean)
    def __init__(self, name, age, breed, temperament, indoor):
        # self.name = name
        # self.age = age
        # self.breed = breed
        # self.temperament = temperament

        # self.indoor = indoor

    # Use super to pass the Pet parameters to the super class (DRY)
        super().__init__(name, age, breed, temperament)

    # Add an indoor attribute
        self.indoor = indoor

# 9. ✅. Create a method unique to the Cat subclass called talk which returns the string "Meow!"
    def say_hello(self):
        print(f"{self.name} says hello")

# 10. ✅. Create a method called print_pet_details to match the print_pet_details in Pet    
        
        # Add super().print_pet_details() and print the indoor attribute
    def print_pet_details(self):
        super().print_pet_details()
        print(f'''
            Indoor: {self.indoor}
        ''')
        