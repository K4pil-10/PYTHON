import random
from jack_logo import  logo


def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return"Lose, the opponent has BlackJack 😱"
    elif u_score == 0:
        return "Win with a BlackJack 😎"

    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score >21:
        return "Opponent went over. You win 😁"

    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    computer_score = -1
    user_score = -1
    isGameOver= False

    for _ in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())

    while not isGameOver:

        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(f"The card of user: {user_cards} and the score is {user_score}")
        print(f"The card of computer: {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isGameOver= True

        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass :")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                isGameOver= True

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score= calc_score(computer_cards)

    print(f"You final cards:{user_cards} and Final Score: {user_score}")
    print(f"Computer final cards:{computer_cards} and Final Score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" *20)
    play_game()
