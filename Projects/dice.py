import random


def main():
    player1 = 0
    player2 = 0
    rounds = 1
    
    while rounds != 4:
        print("Round" + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 roll " + str(player1))
        print("Player 2 roll " + str(player2))

        if player1 == player2:
            print("Draw!\n")
        elif player1 > player2:
            print("Player 1 Wins\n")
        else:
            print("Player 2 wins\n")        

        rounds = rounds + 1

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()
