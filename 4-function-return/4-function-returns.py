def add(a,b):
    return(a +b)

def sub(a,b):
    return a - b

def div(a,b):
    return a/b

def mult(a,b):
    return a * b

# try:
#     guest_1_pancakes = int(input('How many pancakes? '))
#     guest_2_pancakes = int(input('and for your guest? '))
# except:
#     print('That is not a number!')
#     exit()

# total = mult(add(guest_1_pancakes,guest_2_pancakes), 1.12)

# None is a keyword, in JS it is undefined

def pancakes(guests, number_of_pancakes):
    return round((guests * number_of_pancakes) * 1.12)

guests = int(input('How many guests? '))
numberPancakes = int(input('How many pancakes? '))

total = pancakes(guests,numberPancakes)
print(total)

# Temperature Conversion
def fahrenheitToCelsius(temperature):
    return ((temperature - 32) * .5556)

def celsiusToFahrenheit(temperature):
    return ((temperature * 1.8) + 32)

temperature = float(input('What is the fahrenheit temperature you want to convert? '))
temp = fahrenheitToCelsius(temperature)

print(temp)

temperature2 = float(input('What is the celsius you want to convert? '))
temp2 = celsiusToFahrenheit(temperature2)

print(temp2)