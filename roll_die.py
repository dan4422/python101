import random

# Dice Roller
def dice_roller():
    print("Let's roll a dice!")
    user_input = int(input('How many sides should it have? (2-20): '))
    print("It's rolling...")
    dice_roller = random.randrange(1,user_input + 1)
    print(f"It's a {dice_roller}!")
    return dice_roller

# dice_roller()