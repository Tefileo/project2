import random

try_again = 'Yes'
while try_again == 'Yes':


    best_guess = int(input('Is the number im thinking of 1 or 2: '))

    if best_guess == 1 or best_guess == 2:
        random_answer = random.randrange(1,3)

        if best_guess == random_answer:
            print('You WIN!!')
            try_again1 =  input('Would you like to try again? (Yes or No) :').strip().capitalize()
            try_again = try_again1[:3]

        else:
            print('You Lose!, the answer was {}'.format(random_answer))
            try_again1 = input('Would you like to try again? (Yes or No) :').strip().capitalize()
            try_again = try_again1[:3]
    else:
        print('You need to guess a number between 1 and 2')