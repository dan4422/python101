# Print a square
# stars = ['*','*','*','*','*']

# for star in stars:
#     print(star + star + star + star + star)

# Print a triangle pyramid
# height = int(input('How many rows of stars do you want?: '))
# for i in range(height):
#     spaces = height - 1 - i
#     stars = i * 2 + 1
#     print(' ' * spaces + '*' * stars)

# # Multiplication Tables
# for i in range(10):
#     add = i + 1
#     for i in range(10):
#         add2 = i + 1
#         print(f'{add} X {add2} = {add*add2}')

# Print a box
# width = int(input('How wide?: '))
# height = int(input('How high?: '))

# for i in range(height):
#     if i == 0 or i == height - 1: # this is because the height is 5 but range() is exclusive at the end meaning it ends at 4. so you need to subtract 1 to the height(5) to print the last line
#         print('*' * width)
#     else:
#         spaces = width - 2
#         print('*' + ' ' * spaces + '*')

# Coin Flipper
import random

# def coin_flip():
#     coin = ['heads','tails']
#     return random.choice(coin)

# coins = 1
# list = ['yes']
# print('You have 1 coin.')
# while True:
#     answer = input('Do you want another?(yes/no): ')
#     if answer.lower() == 'yes':
#         coins += 1
#         list.append('yes')
#         print(f'You have {coins} coins.')
#     elif answer.lower() == 'no':
#         print("Let's flip them!")
#         for coin in range(coins):
#             print(f'Coin {coin+1} - {coin_flip()}')
#         break

# Guessing Game

