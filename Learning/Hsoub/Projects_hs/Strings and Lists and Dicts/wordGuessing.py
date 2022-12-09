import random

name = input("What is ur name: ")
print("Good luck",name)

names = ['hadi','yara', 'hasan', 'sara', 'osama']

word = random.choice(names)

print('the name is: ')

guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for char in word:
        if char in guesses :
            print(char)
        else:
            print('-')
            failed+=1

    if failed == 0:
        print("you win")
        print('name is', word)
        break

    guess = input("guess a char: ")
    guesses += guess

    if guess not in word:
        turns-=1
        print('wrong')
        print(f'you have {turns} more guesses')

    if turns == 0:
        print('you loose')




