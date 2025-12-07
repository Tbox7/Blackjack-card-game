import blackjack_art
import  function_prog_ver.blackjack_functions as blackjack_functions
## rules + game start ##
print("""
Welcome to BLACKJACK. Please read the rules before playing:
<> Every player is dealt two cards. The goal is to beat the dealer's hand by being the closest to 21.
<> Hit is to be dealt a card. Stand or Stay for when your satisified with your hand. 
<> If you beat the dealer you get double your bet. If you get a blackjack you will be awarded triple the bet. If you lose to dealer your bet will be lost. 
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
    blackjack_functions.game = True

while blackjack_functions.game == True:
    for player in blackjack_functions.players:
        dealer_result = blackjack_functions.dealer_turn()
        blackjack_functions.turn_over = False
        while blackjack_functions.turn_over == False:
            blackjack_functions.print_player_hand(player)
            turn_over , player_status, result = blackjack_functions.player_action(player)
            if player_status == 'BUST':
                print(f"{player} has BUSTED!!!")
                blackjack_functions.countdown(5)
                blackjack_functions.clear()
                blackjack_functions.turn_over = True
            elif player_status == 'STAY':
                if result > dealer_result and result <= 21:
                    blackjack_functions.win(player)
                    print(f"{player} has won!!!")
                    blackjack_functions.countdown(5)
                    blackjack_functions.clear()
                else:
                    print(f"{player} has lost to the dealer!!!")
                    blackjack_functions.countdown(5)
                    blackjack_functions.clear()
                blackjack_functions.turn_over = True
            elif player_status == 'BLACKJACK':
                print(f"{player} has BLACKJACK!!!")
                blackjack_functions.countdown(5)
                blackjack_functions.clear()
                blackjack_functions.blackjack(player)
                blackjack_functions.turn_over = True
    blackjack_functions.reset()
    if input("Next Round: Y/N ").lower() == 'n':
        blackjack_functions.game = False
        print("Thanks for playing!")
    else:
        blackjack_functions.clear()
        print(blackjack_art.logo)
        blackjack_functions.setup()
        blackjack_functions.deal()
        blackjack_functions.dealer()
        blackjack_functions.game = True


