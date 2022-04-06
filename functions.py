#input accepts user input and returns that value as a string
# which can be stored in a variable and used later


# def  say_hello():
#     name = input('What is your name? ')
#     print(f'Hello, {name}!')

# def my_dog(name, age):
#     print(f"My dog's name is {name} and he is {age} years old")


# # say_hello()
# my_dog('nelson', 4)
# my_dog('milo', 8)
# my_dog("Pepe",555)
divider = ''' '''
# User Greeter
# Write a function that accepts two parameters: first_name and last_name. 
# Use those two variables to print a greeting that uses the first_name and last_name variables in the output.
# Call your function after you have defined it and pass in two strings. Do this twice.
def greeting(first_name, last_name):
    print(f'Hello and Goodmorning to you, {first_name} {last_name}!')

greeting('Daniel', 'Lee')
greeting('Lachlan', 'Heywood')

# Email Generator
# Write a function that accepts three parameters, first_name, last_name and domain. 
# Generate a company email address that follows the pattern: "first initial, period, last name @ company domain".  Print the email to the console.
# Call your function after you have defined it and pass in two strings. Do this twice.
def email(first_name, last_name, domain):
    print(f'{first_name[0]}.{last_name}@{domain}')

email('Daniel','Lee','digitalcrafts.com')
email('Lachlan','Heywood','google.com')

# Username Generator
# Write a function. Make it accept two parameters: first_name and last_name. 
# Generate a username and print it to the console. The username should follow this format: first three letters from first_name, underscore, five letters from last_name.

def username(first_name, last_name):
    print(f'{first_name[:3]}_{last_name[:5]}')

username('daniel','lee')
username('lachlan','Heywood')
print(divider)
# New User Contact Information
# Write a function that accepts three parameters, first_name, last_name and domain. 
# Using all the functions you have created so far, call them from inside the new contact card function so that output that looks better than just printing values.

# def contact_card(first_name, last_name, domain):
#     print(f'''Welcome to Digitalcrafts, {first_name}!
#     Email: {first_name[0]}.{last_name}@{domain}
#     Username: {first_name[:3]}.{last_name[:5]}''')

def contact_card(first_name, last_name, domain):
    greeting(first_name, last_name)
    print('Email: ')
    email(first_name, last_name, domain)
    print('Username: ')
    username(first_name, last_name)

contact_card('Daniel', 'Lee', 'digitalcrafts.com')
print(divider)
contact_card('Lachlan','Heywood', 'google.com')
