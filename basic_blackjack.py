import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cards_player=[]
score_player=0
cards_comp=[]
score_comp=0

def start_game():
    global score_player, score_comp
    global cards_player, cards_comp
    choice_user=random.choices(cards, k=2)
    cards_player.append(choice_user[0])
    cards_player.append(choice_user[1])
    choice_comp = random.choices(cards, k=2)
    cards_comp.append(choice_comp[0])
    cards_comp.append(choice_comp[1])
    score_comp +=sum(cards_comp)
    score_player +=sum(cards_player)


def next_turn():
    global score_player
    global cards_player
    next_c_u = random.choice(cards)
    cards_player.append(next_c_u)
    score_player+=next_c_u
    print(f"    Your cards: {cards_player}, current score: {score_player}")
    print(f"    Computer's first card: {cards_comp[0]}")

def computer_turn():
    global score_comp
    global cards_comp
    next_c_c = random.choice(cards)
    cards_comp.append(next_c_c)
    score_comp+=next_c_c

def end_game():
    global score_player, score_comp
    global cards_player, cards_comp
    print(f"    Your cards: {cards_player}, current score: {score_player}")
    if score_player > 21 and score_comp < 21:
        print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
        print(f"You went over. You lose! :c")
    elif score_player <21 and score_comp <=21 and score_player < score_comp:
        print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
        print(f"You lose! :c")
    elif score_player == 21 and score_comp != 21:
        print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
        print(f"You win! c:")
    elif score_player <21 and score_comp >21:
        print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
        print(f"You win! c:")
    elif score_player <21 and score_comp <21 and score_player > score_comp:
        print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
        print(f"You win! c:")
    elif score_player > 21 and score_comp > 21 and score_player < score_comp:
        print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
        print(f"You win! c:")
    elif score_player > 21 and score_comp > 21 and score_player > score_comp:
        print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
        print(f"You went over. You lose! :c")
    elif score_player == score_comp:
        if len(cards_player) == len(cards_comp):
            print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
            print(f"It's a tie!")
        elif len(cards_player) < len(cards_comp):
            print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
            print(f"You win! c:")
        elif len(cards_player) > len(cards_comp):
            print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
            print(f"You lose! c:")

    cards_player= []
    score_player=0
    score_comp=0
    cards_comp = []


play= True
while play:
    play_y_n = input("Do you want to play a game of Blackjack? (y/n)")
    if play_y_n == "n":
        print("Goodbye!")
        play = False
    else:
        start_game()
        if score_player ==21:
            print(f"    Your cards: {cards_player}, current score: 0")
            print(f"    Computer's final hand: {cards_comp}, final score: {score_comp}")
            print(f"Win with a Blackjack! c:")

        else:
            print(f"    Your cards: {cards_player}, current score: {score_player}")
            print(f"    Computer's first card: {cards_comp[0]}")


            continue_pass = input("Type 'y' to get another card, type 'n' to pass:")
            if continue_pass == "y":
                cont_game= True
                while cont_game:
                    next_turn()
                    if score_player > 21:
                        cont_game = False
                    else:
                        continue_pass_l = input("Type 'y' to get another card, type 'n' to pass:")
                        if continue_pass_l == "y":
                            cont_game = True
                        else:
                            cont_game = False
                while score_comp < 17:
                    computer_turn()
                end_game()
            else:
                if score_comp < 17:
                    computer_turn()
                end_game()