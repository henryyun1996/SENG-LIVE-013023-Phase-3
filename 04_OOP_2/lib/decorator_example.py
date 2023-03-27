import ipdb

# 1. ✅ First Class Functions
# "[We can] assign them to variables, store them in data structures, pass them as arguments
# to other functions, and even return them as values from other functions."
# See more => http://bit.ly/3YQh8KR

    # Create functions to be used as callbacks 

# def walk(pet):
#     print(f"{pet} walked!")

# def feed(pet):
#     print(f"{pet} fed!")

    # Create a higher-order function that will take a callback as an argument

# def execute_task(func):
#     return func("Rose")

# ipdb.set_trace()

# 2. ✅ Create a higher-order function that declares / returns an inner function

# def higher_order_function():
#     def inner_function():
#         print("Hello from within")
#     return inner_function

# ipdb.set_trace()

# def execute_task():
#     def walk(pet):
#         print(f"{pet} Walked!")
#     return walk
# walk = execute_task()
# walk("Rose")

# 3. ✅ Decorator

# Create a decorator (coupon_calculator) that:
    # - takes a function as an argument
    # - has an inner function defined 
    # - returns the inner function

# Tools:

    # .format()
    # https://www.geeksforgeeks.org/python-string-format-method/

    # .round()
    # https://www.geeksforgeeks.org/round-function-python/

def coupon_calculator(func):
    def report_price():
        print("Initial price = $35.00")
        final_price = func(35.00)
        print(f"Newly discounted Price: {final_price}")
    return report_price

# Try using a decorator with / without pie syntax '@'

# Create Decorator (coupon_calculator)

# Create Callback Function to Calculate New Price (calculate_price)

# Without pie syntax 

    # report_price = coupon_calculator(calcuate_price)
    # report_price()

# With pie syntax
    # @decorator
    # def some_func():
        # ...
    # cb_function()

@coupon_calculator
def calculate_price(price):
    
    # :.2f => Format Price as 2 Decimal Point Floating Number
    # :.3f => Format Price as 3 Decimal Point Floating Number
    
    return '{:.2f}'.format(round(price / 2, 2))

# report_price = coupon_calculator(calculate_price)
# report_price()
    
calculate_price()