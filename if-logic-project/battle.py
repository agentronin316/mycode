#! usr/bin/env python3

from random import randint

warriors = [
    {"class": "Fighter",
    "might": 5, "magic": 2, "speed": 3, "health": 10}

]

def main():
    warrior=""
    while True:
        print("Choose your warrior!")
        for i in range(0,len(warriors)):
            print(f"{i + 1}: {warriors[i]['class']}")
            print(f"Might: {warriors[i]['might']}")
            print(f"Magic: {warriors[i]['magic']}")
            print(f"Speed: {warriors[i]['speed']}")
            print(f"Health: {warriors[i]['health']}")
            if i != len(warriors) - 1:
                input("press Enter to continue")
        try:
            player= warriors[int(input("Enter the number for your combatant: ")) - 1]
            break
        except:
            input("invalid selection, press Enter to review choices")
    opponent = warriors[randint(0, len(warriors) - 1)]
    player["curHealth"]= player["health"]
    player["time"]= 0
    opponent["curHealth"]= opponent["health"]
    opponent["time"]= 0
    combat(player,opponent)

def combat(player,opponent):
    while ((player["curHealth"] > 0) & (opponent["curHealth"] > 0)):
        player["time"] += player['speed']
        opponent["time"] += opponent['speed']
        print(f"player: {player['time']} AI: {opponent['time']}")
        print(f"{player['curHealth']}, {opponent['curHealth']}")
        while player['time'] >= 25:
            player['time'] -= 25
            opponent['curHealth'] -= playerTurn(player)

        while opponent['time'] >= 25:
            print("AI Turn")
            opponent['time'] -= 25
            player['curHealth'] -= opponentTurn(opponent)
    if(opponent['curHealth'] <= 0):
        print("Congratulations, You Win!")
    else:
        print("Too bad, Computer Wins!")

def playerTurn(player):
    print("playerTurn placeholder")
    return 1

def opponentTurn(opponent):
    print("opponentTurn placeholder")
    return 1


main()