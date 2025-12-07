import os
import random
import blackjack_art 
import time
cards = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
dealer_hand = []
game_bets = {}
players ={}
game = False
turn_over = False
def reset():
    """Resets all variables to 0"""
    dict.clear(game_bets)
    list.clear(dealer_hand)
    for i in players:
        players[i]['cards'] = []

def dealer_turn():
    """This is gonna be the hit for the dealer | this will have a soft 17"""
    dealer_hand = []
    result = 0
    for value in dealer_hand:
       result += value
    while result <=17:
        card_value = random.choice(cards)
        dealer_hand.append(card_value)
        result += card_value
    if (result >= 21 or result >= 17) and 11 in dealer_hand:
        dealer_hand = [1 if x == 11 else x for x in dealer_hand]
        dealer_turn()
    return result

def print_hand(player):
    """This will print the current hand of the player"""
    for i in players[player]['cards']:
        print(blackjack_art.cards[i])

def win(player):
    """This function computes when you beat dealer"""
    bet = game_bets[player]
    bet *=2
    curr_coins = int(players[player]['coins']) 
    curr_coins+= bet
    players[player]['coins'] = str(curr_coins)

def blackjack(player):
    """This funciton computes when you get a blackjack (perfect 21)"""
    bet = game_bets[player]
    bet *=3
    curr_coins = int(players[player]['coins']) 
    curr_coins+= bet
    players[player]['coins'] = str(curr_coins)

def print_dealer_hand():
    print("<><><><><><><><><><><><><><><><><><><>")
    print("<><><><><><> DEALER HAND <><><><><><>")
    print("<><><><><><><><><><><><><><><><><><><>")
    for card in dealer_hand:
        print(blackjack_art.cards[card])
    print("<><><><><><><><><><><><><><><><><><><>")

def dealer_hand_hidden():
    print("<><><><><> DEALER HAND <><><><><><>")
    print("<><><><><><><><><><><><><><><><><><><>")
    print(blackjack_art.cards[dealer_hand[1]])
    print(blackjack_art.blank)
    print("<><><><><><><><><><><><><><><><><><>")
    print("<><><><> LETS GET STARTED <><><><><>") 
    print("<><><><><><><><><><><><><><><><><><>")

def hit(player):
    """This funciton deals a card to player"""
    new_card = random.choice(cards)
    players[player]['cards'].append(new_card)
    clear()
    print(blackjack_art.logo)
    dealer_hand_hidden()
    print_player_hand(player)

def dealer():
    """This function is the dealer and its calculations"""
    one = int(random.choice(cards))
    two = int(random.choice(cards))
    dealer_hand.append(one)
    dealer_hand.append(two)
    dealer_hand_hidden()
    
def create_player(num):
    """This function creates a player with input(name)"""
    for i in range(1,num+1):
        temp_name = ('player'+str(i)) 
        temp_name = {}  
        temp_name['cards'] =[]
        temp_name["coins"] = 1000
        players['player'+str(i)] = temp_name

def setup():
    """This function will setup the game with the inital bids"""
    for i in (players):
        print(f"{i} you have {players[i]['coins']}.")
        bet = int(input(f'{i} bet: '))
        players[i]['coins'] = players[i]['coins'] - bet
        game_bets[str(i)] = (f" has bet {bet}")
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

def clear():
    """clears terminal"""
    os.system('cls' if os.name=='nt' else 'clear')
    return("   ")

def player_action(player):
    """This function will take the player input and do the action"""
    result = 0
    turn_over = False
    player_status = ''
    for card in players[player]['cards']:
        result += card
    if result == 21:
        turn_over = True
        player_status = 'BLACKJACK'
        return turn_over, player_status, result
    elif result >=21:
        turn_over = True
        player_status = 'BUST'
        return turn_over, player_status, result
    else:
        ans = input(f"{player} What would you like to do? |'h' is to hit|'s' is to stay:  ")
        if ans == 'h':
            hit(player)
            player_action(player)
        elif ans == 's':
            turn_over = True
            player_status = 'STAY'
        return turn_over, player_status, result
    

def print_player_hand(player):
    """This function will print the player hand"""
    print("<><><><><><><><><><><><><><><><><><>")
    print((f"{player} has: "))
    for i in players[player]['cards']:
        print(blackjack_art.cards[i])
    print("<><><><><><><><><><><><><><><><><><>")


def countdown(seconds):
    while seconds:
        time.sleep(1)
        seconds -= 1
