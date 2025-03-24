import random
import art

deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]

def checker(p_total, c_total, p, c):
    print(f"Your final hand: {p}, final score: {p_total}")
    print(f"Computer's final hand: {c}, final score: {c_total}")
    if p_total > 21:
        print("You went over. You lose")
    elif c_total > 21:
        print("Computer went over. You win")
    elif p_total > c_total:
        print("You're higher. You win")
    elif c_total > p_total:
        print("Computer is higher. You lose")
    elif p_total == c_total:
        print("It's a draw")
    elif c_total == 21 and len(c) == 2 and (11 in c) and (10 in c):
        print("Computer has a Blackjack. You lose")
    

def output(p_total, p, c):
    print(f"Your cards: {p}, current score: {p_total}")
    print(f"Computer's first card: {c[0]}")

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play == 'y':
    print(art.logo)
    player = []
    computer = []
    for i in range(2):
        player.append(random.choice(deck))
    computer.append(random.choice(deck))
    player_total = sum(player)
    computer_total = sum(computer)

    if player_total == 21:
        output(player_total, player, computer)
        print(f"Your final hand: {player}, final score: 0")
        print(f"Computer's final hand: {computer}, final score: {computer_total}")
        print("Win with a Blackjack")
    else:
        if player_total > 21 and (11 in player):
            player[player.index(11)] = 1
            player_total = sum(player)
        output(player_total, player, computer)

        action = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while action == "y":
            player.append(random.choice(deck))
            player_total = sum(player)
            if player_total > 21 and (11 in player):
                player[player.index(11)] = 1
                player_total = sum(player)
                output(player_total, player, computer)
                action = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            elif player_total > 21:
                action = "n"
                output(player_total, player, computer)
            else:
                output(player_total, player, computer)
                action = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if action == "n" and player_total < 21:
            while computer_total < 17:
                computer.append(random.choice(deck))
                computer_total = sum(computer)

        checker(player_total, computer_total, player, computer)

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    print("\n" * 500)
