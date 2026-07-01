import random





fist= r'''       
        ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
        `----- '''

paper = r'''
                     _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
                    |     | '''
                    
scissors = r'''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/ '''
  
  

print("Welcome to Rock, Paper, Lesbian!")
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

if user_choice == "0":
    print("You chose Rock!")
    print(fist)
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose Rock!")
        print(fist)
        print("It's a tie!")
    elif computer_choice == 1:
        print("Computer chose Paper!")
        print(paper)
        print("You lose!")
    else:
        print("Computer chose Scissors!")
        print(scissors)
        print("You are a Lesbian!")
    
    
elif user_choice == "1":
    print("You chose Paper!")
    print(paper)
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose Rock!")
        print(fist)
        print("You win!")
    elif computer_choice == 1:
        print("Computer chose Paper!")
        print(paper)
        print("It's a tie!")
    else:
        print("Computer chose Scissors!")
        print(scissors)
        print("You lose!")
elif user_choice == "2":
    print("You chose Scissors!")
    print(scissors)
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose Rock!")
        print(fist)
        print("You lose!")
    elif computer_choice == 1:
        print("Computer chose Paper!")
        print(paper)
        print("You are a Lesbian!")
    else:
        print("Computer chose Scissors!")
        print(scissors)
        print("It's a tie!")
else:
    print("Invalid choice. Please try again.")