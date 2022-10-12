import blackjack_art
import  blackjack_functions
## rules + game start ##
print("""
Welcome to BLACKJACK. Please read the rules before playing:
<> Every player is dealt two cards. The goal is to beat the dealer's hand by being the closest to 21.
<> Hit is to be dealt a card. Stand or Stay for when your satisified with your hand. Double down is a chance to double your bet before you declare to stand or stay.
<> If you beat the dealer you get half of your bet. If you get 21 it's a blackjack and will be awarded double the bet. If you lose to dealer your bet will be lost. 
<> You lose when you run out of coin or type "quit". Everyone starts with 1000. Have fun and good luck!!!
""")
#setup the game after typing 'ready'
if (input("Type 'ready' when you have read the rules. : ").lower()) == 'ready':
    blackjack_functions.create_player(int(input("Input the number of players: ")))
    blackjack_functions.clear()
    print(blackjack_art.logo)
    blackjack_functions.setup()
    blackjack_functions.deal()
    blackjack_functions.dealer()


current_player = ()
for i in blackjack_functions.players:
    current_player = i
    turn = False
    while turn == False:
        print(f'{i} has: ')
        blackjack_functions.print_hand(i)
        action = input(f"{i} What would you like to do? |'h' is to hit|'s' is to stay or stand|'dd' is to double down|:  ")
        if action == 'h':
            blackjack_functions.players[i]['cards'].append( blackjack_functions.hit())
        elif action == 's':
            blackjack_functions.clear()
            print(blackjack_art.logo)
            blackjack_functions.print_dealer_hand()
            break
        elif action == 'dd':
            blackjack_functions.players[i]['cards'].append( blackjack_functions.doube_down(i))
            blackjack_functions.clear()
            print(blackjack_art.logo)
            blackjack_functions.print_dealer_hand( )
            break

blackjack_functions.dealer_turn()

game_score = []
for i in blackjack_functions.players:
    x = 0
    for t in blackjack_functions.players[i]['cards']:
        x = t+x
    if x > 21:
        game_score.append(f'{i}: BUST')
    elif x == blackjack_functions.dealer_turn():
        game_score.append(f'{i}: PUSH')
        blackjack_functions.push(i)
    elif x == 21:
        game_score.append(f'{i}: BLACKJACK')
        blackjack_functions.blackjack(i)
    elif x > blackjack_functions.dealer_turn():
        game_score.append(f'{i}: WIN')
        blackjack_functions.win(i)
    elif x < blackjack_functions.dealer_turn():
        game_score.append(f'{i}: BUST')

blackjack_functions.clear()
print(blackjack_art.logo)
print(game_score)
blackjack_functions.reset()
print(blackjack_functions.players)

game = True
while game == True:
    next_round = input("Type 'y' for next round: ")
    if next_round == 'y':
        print(blackjack_art.logo)
        blackjack_functions.setup()
        blackjack_functions.deal()
        blackjack_functions.dealer()
        current_player = ()
        for i in blackjack_functions.players:
            current_player = i
            turn = False
            while turn == False:
                print(f'{i} has: ')
                blackjack_functions.print_hand(i)
                action = input(f"{i} What would you like to do? |'h' is to hit|'s' is to stay or stand|'dd' is to double down|:  ")
                if action == 'h':
                    blackjack_functions.players[i]['cards'].append( blackjack_functions.hit())
                elif action == 's':
                    blackjack_functions.clear()
                    print(blackjack_art.logo)
                    blackjack_functions.print_dealer_hand()
                    break
                elif action == 'dd':
                    blackjack_functions.players[i]['cards'].append( blackjack_functions.doube_down(i))
                    blackjack_functions.clear()
                    print(blackjack_art.logo)
                    blackjack_functions.print_dealer_hand( )
                    break
        game_score = []
        for i in blackjack_functions.players:
            x = 0
            for t in blackjack_functions.players[i]['cards']:
                x = t+x
            if x > 21:
                game_score.append(f'{i}: BUST')
            elif x == blackjack_functions.dealer_turn():
                game_score.append(f'{i}: PUSH')
                blackjack_functions.push(i)
            elif x == 21:
                game_score.append(f'{i}: BLACKJACK')
                blackjack_functions.blackjack(i)
            elif x > blackjack_functions.dealer_turn():
                game_score.append(f'{i}: WIN')
                blackjack_functions.win(i)
            elif x < blackjack_functions.dealer_turn():
                game_score.append(f'{i}: BUST')
        blackjack_functions.clear()
        print(blackjack_art.logo)
        print(game_score)
        print(blackjack_functions.players)
        blackjack_functions.reset()


