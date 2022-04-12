from flip_coin import coin_flip
from roll_die import dice_roller
import random

def game_helper():
    list = []
    while True:
        list_of_players = input("Enter a player's name to include or type in no: ")
        list.append(list_of_players)
        if list_of_players == 'no':
            break
        print(list)
    while True:
        user_input = input("""Please choose an option: 
    0 - start new round
    1 - flip a coin
    2 - roll a die
    3 - roll multiple dice
    4 - randomly choose a user
    q - exit
    """)
        if user_input == '0':
            for player in list:
                print(player)
                enter = input('Press enter to continue: ')
                if enter == '':
                    game_helper()
        elif user_input == '1':
            coin_flip()
        elif user_input == '2':
            dice_roller()
        elif user_input == '3':
            number_dice = int(input('Select how many dice to roll?: '))
            total_dice = 0
            for number in range(number_dice):
                total_dice += dice_roller()
            print(f'The total of dice is {total_dice}')
        elif user_input == '4':
            print(random.choice(list))
        elif user_input == 'q':
            break
        else:
            print('Try again!')
    print('Goodbye!')

game_helper()