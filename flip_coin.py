import random

def coin_flip():
    coin = ['heads','tails']
    print('You flipped a coin!')
    print(f'It is {random.choice(coin)}!')