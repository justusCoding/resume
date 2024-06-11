def RPS_function():
    import random


    rps = ["rock","paper","scissors"]
    roundsplayed = 0

    user1Wins = 0
    user2Wins = 0


    while roundsplayed <=3 or user1Wins < 2 or  user2Wins <2 :
        
        
        user1move = random.choice(rps)
        user2move = random.choice(rps)

        print("Player 1 chose:", user1move)
        print("Player 2 chose:", user2move)


        if user1move == user2move:
            print("It's a tie!")
        elif (user1move == "rock" and user2move == "scissors") or \
            (user1move == "paper" and user2move == "rock") or \
            (user1move == "scissors" and user2move == "paper"):
            print("Player 1 wins!")
            user1Wins += 1
        else:
            print("Player 2 wins!")
            user2Wins += 1
        
        roundsplayed += 1

        
        if user1Wins >= 2:
            print(f"Player 1 wins best 2/3")
            break
        elif user2Wins >= 2:
            print(f"Player 2 wins best 2/3")
            break
        
RPS_function