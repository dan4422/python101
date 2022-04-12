#Count to X
# count = int(input('Enter a number: '))
# number = 0
# while number < count:
#     number += 1
#     print(number)

# # Count N to M
# count = int(input('Enter a number: '))
# number = int(input('Enter another number: '))
# while count <= number:
#     count += 1
#     print(count-1)

# count = int(input('Enter a number: '))
# number = int(input('Enter another number: '))
# if count <= number:
#     while count <= number:
#         print(count)
#         count += 1
# elif count >= number:
#     while count >= number:
#         print(count)
#         count -= 1
# else:
#     print('error')

# Count odd to N to M
# count = int(input('Enter a number: '))
# number = int(input('Enter another number: '))
# if count <= number:
#     while count <= number:
#         if (count % 2) != 0:
#             print(count)
#         count += 1
# elif count >= number:
#     while count >= number:
#         if (count % 2) != 0:
#             print(count)
#         count -= 1
# else:
#     print('error')

# #Fizzbuzz
# number = int(input('Enter a number: '))
# count = 0
# while count <= number:
#     if (count % 3) == 0 and (count % 5) == 0:
#         print('fizzbuzz')
#     elif (count % 5) == 0:
#         print('Buzz')
#     elif (count % 3) == 0:
#         print('fizz')
#     else:
#         print(count)
#     count += 1

#Grandma CLI
while True:
    ask = input('What do you want to say to grandma?: ')
    if ask == 'BYE':
        print('BYE GRANDSON!')
        break
    elif ask == ask.upper():
        print('NO, NOT SINCE 1938!')
    else:
        print('HUH?! SPEAK UP, SONNY!')
