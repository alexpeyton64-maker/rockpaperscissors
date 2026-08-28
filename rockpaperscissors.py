import random
choices = ['r', 'p', 's']
user_choice = input('Rock, paper, or scissors? (r/p/s)')
if user_choice not in choices:
    print('Invalid choice!')
computer_choice = random.choice(choices)
if user_choice == 'r':
    print('')
print(f'You chose {user_choice}')
print(f'Computer chose {computer_choice}')
