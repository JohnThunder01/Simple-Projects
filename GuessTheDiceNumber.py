import random

dice_1_result = input('Enter your guess for Dice 1: ')
dice_2_result = input('Enter your guess for Dice 2: ')

min_Val = 1
max_Val = 6

random_1 = random.randint(min_Val, max_Val)
str(random_1)
random_2 = random.randint(min_Val, max_Val)
str(random_2)

print("Dices Rolling......")
if dice_1_result == random_1:
    print(f'You win, It was {random_1}')
else:
    print(f'You loose, It was actually {random_1}')

if dice_2_result == random_2:
    print(f'You win, It was {random_2}')
else:
    print(f'You loose, It was actually {random_2}')
