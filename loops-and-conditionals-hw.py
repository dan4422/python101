import random

# # Coin Flip
def coin_flip():
    coin = ['heads','tails']
    print('You flipped a coin!')
    print(f'It is {random.choice(coin)}!')
    
# coin_flip()

# # Even Odd
# def even_odd(input):
#     if (input % 2) != 0:
#         return True
#     else:
#         return False

# user_input = int(input('Enter a number: '))

# if even_odd(user_input) == True:
#     print('The number is odd!')
# else:
#     print('The number is even!')

# # Dice Roller
def dice_roller(num1,num2):
    return random.randrange(num1,num2)

print("Let's roll a dice!")
user_input = int(input('How many sides should it have? (2-20): '))
print("It's rolling...")
print(f"It's a {dice_roller(1,user_input + 1)}!")