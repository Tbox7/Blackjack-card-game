import os
import random
import blackjack_art
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer_hand = []
game_bets = {}
players ={}

def reset():
    """Resets all variables to 0"""
    game_bets = {}
    dealer_hand = []
    for i in players:
        players[i]['cards'] = []

def doube_down(player):
    """This function is to double the money you have bet"""
    new_card = random.choice(cards)
    bet = game_bets[player]
    players[player]['coins'] -= bet
    bet += bet
    game_bets[player] = bet
    return new_card

def dealer_turn():
    """This is gonna be the hit for the dealer | this will have a soft 17"""
    #delete if i can make the hit() function also work with the dealer list. 
    #return the number value of the dealer
    #if dealer goes over return 0
    x = 0
    for i in dealer_hand:
        x += i
        if x == 21:
            return x
        elif x>21:
            return 0
        elif x<17:
            dealer_hand.append(random.choice(cards))
        else:
            return x
    
def print_hand(num):
    """This will print the current hand of the player"""
    for i in players[num]['cards']:
        if i == 10: 
            print(blackjack_art.random.choice(blackjack_art.cards[10]))
        if i != 10:   
            print(blackjack_art.cards[i])

def win(player):
    """This function computes when you beat dealer"""
    bet = game_bets[player]
    bet = bet+bet
    players[player]['coins'] += bet

def blackjack(player):
    """This funciton computes when you get a blackjack (perfect 21)"""
    bet = game_bets[player]
    bet = bet+bet+bet
    players[player]['coins'] += bet

def push(player):
    bet = game_bets[player]
    players[player]['coins'] += bet

def print_dealer_hand():
    print("<><><><><><><><><><><><><><><><><><><>")
    print("<><><><><> DEALER HAND <><><><><><>")
    print("<><><><><><><><><><><><><><><><><><><>")
    if dealer_hand[0] != 10:
        print(blackjack_art.cards[dealer_hand[0]])
    elif dealer_hand == 10:
        print(blackjack_art.random.choice(blackjack_art.cards[10]))
    print("<><><><><><><><><><><><><><><><><><><>")

def hit():
    """This funciton deals a card to player"""
    new_card = random.choice(cards)
    clear()
    print(blackjack_art.logo)
    print(print_dealer_hand())
    return new_card

def dealer():
    """This function is the dealer and its calculations"""
    one = int(random.choice(cards))
    two = int(random.choice(cards))
    dealer_hand.append(one)
    dealer_hand.append(two)
    print("<><><><><> DEALER HAND <><><><><><>")
    print("<><><><><><><><><><><><><><><><><><><>")
    if one == 10 and two != 10:
        print(blackjack_art.random.choice(blackjack_art.cards[10]))
    if two == 10 and one != 10:
        print(blackjack_art.cards[one])
    if two != 10 and one != 10:   
        print(blackjack_art.cards[one])
    if two == 10 and one == 10:
        print(blackjack_art.random.choice(blackjack_art.cards[10]))
    print(blackjack_art.blank)
    print("<><><><><><><><><><><><><><><><><><>")
    print("<><><><> LETS GET STARTED <><><><><>") 
    print("<><><><><><><><><><><><><><><><><><>")

def create_player(num):
    """This function creates a player with input(name)"""
    emp = {}
    for i in range(1,num+1):
        emp['cards'] =[]
        emp["coins"] = 1000
        players['player'+str(i)] = emp
        emp= {}

def setup():
    """This function will setup the game with the inital bids"""
    for i in players:
        print(f"{i} you have {players[i]['coins']}.")
        bet = int(input(f'{i} bet: '))
        players[i]['coins'] = players[i]['coins'] - bet
        game_bets[str(i)] = (bet)
    clear()
    print(blackjack_art.logo)
    print(game_bets)

def deal():
    """This function deals initial cards"""
    for i in players:
        one = int(random.choice(cards))
        two = int(random.choice(cards))
        players[i]['cards'].append(one)
        players[i]['cards'].append(two)
        print("<><><><><><><><><><><><><><><><><><>")
        print(i)
        if one == 10 and two != 10:
            print(blackjack_art.random.choice(blackjack_art.cards[10]))
            print(blackjack_art.cards[two])
        if two == 10 and one != 10:
            print(blackjack_art.cards[one])
            print(blackjack_art.random.choice(blackjack_art.cards[10]))
        if two != 10 and one != 10:   
            print(blackjack_art.cards[one])
            print(blackjack_art.cards[two])
        if two == 10 and one == 10:
            print(blackjack_art.random.choice(blackjack_art.cards[10]))
            print(blackjack_art.random.choice(blackjack_art.cards[10]))
    print("<><><><><><><><><><><><><><><><><><>")

def clear():
    """clears terminal"""
    os.system('cls' if os.name=='nt' else 'clear')
    return("   ")
