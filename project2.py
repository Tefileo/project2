import random

try_again = 'Yes'
while try_again == 'Yes':
    best_guess = int(input('Is the number im thinking of 1 or 2: '))
    random_answer = random.randrange(1,3)
    if best_guess == random_answer:
        print('You WIN!!')
        try_again =  input('Would you like to try again? (Yes or No) :')
    else:
        print('You Lose!, the answer was {}'.format(random_answer))
        try_again =  input('Would you like to try again? (Yes or No) :')

# Comment again