#Work or Sleep in
day = input('What day is it?: ')
day_lower = day.lower()

if (day_lower == 'monday' 
or day_lower == 'tuesday' 
or day_lower == 'wednesday' 
or day_lower == 'thursday' 
or day_lower == 'friday'
):
    print('go to work!')
elif day_lower == 'saturday' or day_lower == 'sunday':
    print('sleep in!')
else:
    print('enter a valid day')

# Secret Password
password = input('Enter Password: ')

if password == 'milo':
    print('Welcome!')
else:      
    print('Try again!')

# Day of week
num = int(input('Enter a number between 1 to 7: '))

if num == 1:
    print('Sunday')
elif num == 2:
    print('Monday')
elif num == 3:
    print('Tuesday')
elif num == 4:
    print('Wednesday')
elif num == 5:
    print('Thursday')
elif num == 6:
    print('Friday')
elif num == 7:
    print('Saturday')
else:
    print('Error!')

#Letter Grade
score = int(input('Enter a score number between 0-100: '))

if score < 60:
    print('F')
elif score < 70:
    print('D')
elif score < 80:
    print('C')
elif score < 90:
    print('B')
elif score >= 90 and score <= 100:
    print('A')
else:
    print('Error')

#Picnic Game
def match(a,b):
    if a[0] == b[0]:
        print('You can come to the party!')
    else:
        print('Try again!')

def match(a,b):
    return a[0] == b[0]

a = input('What is your name?: ')
b = input('What food are you bringing to the party?: ')

if match(a,b) == True:
    print('You can come to the party')
else:
    print('You cannot come to the party')

#Username length validator
def user(username):
    if len(username) > 3 and len(username) < 18:
        print('Valid')
    else:
        print('Not Valid')

def user(username):
    return len(username) > 3 and len(username) < 18

username = input('What is your username?: ')

if user(username) == True:
    print('Valid')
else:
    print('Not Valid')

#Odd and Divisible by 3

def numberFunction(input):
    return input % 2 != 0 and input % 3 == 0

input = int(input('Type in a number: '))

if numberFunction(input) == True:
    print('Success!')
else:
    print('Fail!!')

#Bonus - Match Statements NEED PYTHON VERSION 3.10 or higher
#when can you use a match statement? you can use it instead of multiple elif's
#What does the syntax look like? like a if and elif statement but instead of if its match and instead of elif its case basically
#why is match statement useful? its useful when you have multiple elif's and you want to shorten it

# score = int(input('Enter a score number between 0-100: '))

# match score:
#     case 60:
#         print('F')
#     case 70:
#         print('D')