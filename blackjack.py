import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def draw():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def ace_check(score,deck):
    if score<22:
        return score
    else:
        if 11 in deck:
            index=deck.index(11)
            deck[index]=1
            score-=10
            return score
        return score
def play(score,deck,n):
    inp = input("Type 'y' to get another card, 'n' to pass: ")
    if inp =='y':
        card=draw()
        deck.append(card)
        score+=card
        score = ace_check(score,deck)
        if score>21:
            return score
        else:
            print(f"Your cards: {deck}, current score: {score}")
            print(f"Computer's first card: {n}")
            return play(score,deck,n)
    else:
        return score   

        
def main():
    print(logo)
    comp_cards=[]
    comp_score=0
    while comp_score<17:
        card =draw()
        comp_score+=card
        comp_cards.append(card)
        comp_score=ace_check(comp_score,comp_cards)
    player_cards=[]
    player_score=0
    card=draw()
    player_cards.append(card)
    player_score+=card
    card=draw()
    player_cards.append(card)
    player_score+=card
    player_score=ace_check(player_score,player_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Compter's first card: {comp_cards[0]}")
    player_score = play(player_score,player_cards,comp_cards[0])
    if player_score>21:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: [{comp_cards[1]}], final score: {comp_cards[1]}")
        print("You went over.You lose")
    else :
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
        if comp_score>21:
            print("Opponent wen over.You win")
        elif player_score==comp_score:
            print("Draw")
        elif player_score>comp_score:
            print("You win")
        elif player_score<comp_score:
            print("You lose")
    s = input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")
    if s=='y':
        os.system('cls')
        main()     

s = input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")
if s=='y':
     main()