import random
first_dice = random.randint(1,6)
second_dice = random.randint(1,6)
sum = first_dice+second_dice
print('The sum of dice is ', first_dice ,'+',second_dice ,'=', sum)

if sum == 7 or sum == 11:
    print('You won')
elif sum == 2 or sum == 3 or sum == 12:
    print('Casino won')
else:
    print('Now your goal number is', sum)
    goal_number = sum
    sum = 1
    while sum != goal_number:
        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)
        sum = first_dice+second_dice
        print('The sum of dice is ', first_dice ,'+',second_dice ,'=', sum)
        if sum == 7:
            print('You lose')
            break
        elif sum == goal_number:
            print('You won')
            break
