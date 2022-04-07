

# print(3 + 3)


# # assignment operators
# num = 10

# # addition assignment operators
# num += 1
# print(num)

# num -= 4
# num *= 2
# num /= 3
# print(num) 
# name = "Nelson"
# age = 4.1 # float
# weight = 12 # integer 
# print("Nelson is " + str(age)) # TypeError

# age = "10"
# # print(age * 5) # This would spit out 1010101010
# new_age = int(age) * 5
# print(new_age)

# age = "2.5"
# # print(age * 5) # This would spit out 1010101010
# new_age = float(age) * 5
# print(new_age)

def add(a,b):
    print(a + b)

def subtract(a,b):
    print(a - b)

def multiply(a,b):
    print(a * b)

def divide(a,b):
    print(a/b)

# Pancake Calculator
def pancakes(guests, number_of_pancakes):
    amount = round((guests * number_of_pancakes) * 1.12)
    print(amount)

pancakes(10,3)

# Temperature Conversion
def fahrenheitToCelsius(temperature):
    print(((temperature - 32) * .5556))

def celsiusToFahrenheit(temperature):
    print(((temperature * 1.8) + 32))

fahrenheitToCelsius(100)
celsiusToFahrenheit(0)

# #Gas Conversion
# def gas_conversion(au,us):
#     usPrice = au * .75
    
    



# #Equity Calculator
def equity(years_worked, valuation):
    total_shares = 10,000,000
    ((valuation/total_shares) * (2500*years_worked))

equity(2,50000)
