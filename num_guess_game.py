import random
logo= r"""
 _____ _   _ _____ _____ _____ _ _ _ 
|  __ \ | | |  ___/  ___/  ___| | | |
| |  \/ | | | |__ \ `--.\ `--.| | | |
| | __| | | |  __| `--. \`--. \ | | |
| |_\ \ |_| | |___/\__/ /\__/ /_|_|_|
 \____/\___/\____/\____/\____/(_|_|_)

"""
print(logo)
print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
lvl=input("Choose a difficulty. Type 'easy' or 'hard': ")

num_game=random.randint(1,100)

if lvl == 'easy':
    lives = 10
else:
    lives = 5

win=False

while lives>0 and win==False:
    print(f"You have {lives} attempts left")
    guess=int(input("Make a guess: "))
    if guess==num_game:
        print("You guessed the number!")
        win=True
    elif guess<num_game:
        print("Too low")
        lives-=1
    elif guess>num_game:
        print("Too high")
        lives -= 1