# # User Greeter
# # Define two variables: firstname and lastname.
firstname = 'Daniel'
lastname = 'Leeeeeeee'
# # Assign some string values to the variables. You can use your own name or someone else's. 
# # Use those two variables to print a greeting that uses the firstname and lastname variables in the output.
# greeting = "Good Morning! " + firstname + ' ' + lastname + '!'
# print(greeting)

# # Email Generator
# # Using the two variables you set earlier, generate a company email address that follows the pattern: "first initial, period, last name @ company domain".
# # Assign the result to a new variable called email and print the email to the console.
email = firstname[0] + '.' + lastname + '@digitalcrafts.com'
# print(email)

# # Username Generator
# # Using the firstname and lastname variables, generate a username to a new variable and print it to the console. 
# # The username should follow this format: first three letters from firstname, underscore, five letters from lastname.
username = firstname[:3] + '_' + lastname[:5]
print(username.lower())

# # New User Contact Information
# # Using all the information you have created, print the data in a nice format. 
# # That is, generate a "Contact Card" style output that looks better than just printing values.

# print(greeting)
# print('Email: ' + email)
# print('Username: ' + username)

# f-strings
print(f'hello {firstname}__.__{lastname}')
print(f'Greetings welcome to the company! {firstname} {lastname}')
print(f'Email: {email}')
print(f'Username: {username}')
print(f'''hi

hello

{firstname}

{lastname}

''')
