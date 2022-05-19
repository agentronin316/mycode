#! usr/bin/env python3

from random import randint

warriors = [
    {"class": "Fighter",
    "might": 5, "magic": 2, "speed": 3, "health": 20},
    {"class": "Mage",
    "might": 2, "magic": 5, "speed": 4, "health": 10},
    {"class": "Spell-Blade",
    "might": 4, "magic": 4, "speed": 5, "health": 15},

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
            player= warriors[int(input("Enter the number for your combatant: ")) - 1].copy()
            break
        except:
            input("invalid selection, press Enter to review choices")
    opponent = warriors[randint(0, len(warriors) - 1)].copy()
    player["curHealth"]= player["health"]
    player["time"]= 0
    opponent["curHealth"]= opponent["health"]
    opponent["time"]= 0
    combat(player,opponent)

def combat(player,opponent):
    while ((player["curHealth"] > 0) & (opponent["curHealth"] > 0)):
        player["time"] += player['speed']
        opponent["time"] += opponent['speed']
        while player['time'] >= 25:
            player['time'] -= 25
            opponent['curHealth'] -= playerTurn(player)
            print(f"Opponent is now at {opponent['curHealth']}/{opponent['health']}")

        while opponent['time'] >= 25:
            opponent['time'] -= 25
            player['curHealth'] -= opponentTurn(opponent)
            print(f"You are now at {player['curHealth']}"/{player['health']})

    if(opponent['curHealth'] <= 0):
        print("Congratulations, You Win!")
    else:
        print("Too bad, Computer Wins!")

def playerTurn(player):
    while True:
        choice= input(f"[p]hysical ({player['might']} damage) or [m]agical ({player['magic']} damage)").lower()
        if choice != "":
            if choice[0] == "p":
                print(f"You smack your opponent for {player['might']} damage!")
                return player['might']
            if choice[0] == "m":
                print(f"You blast your opponent for {player['magic']} damage!")
                return player['magic']

def opponentTurn(opponent):
    choice= randint(1,100)
    if choice <= 50:
        print(f"You get smacked for {opponent['might']} damage!")
        return opponent['might']
    else:
        print(f"You get blasted for {opponent['magic']} damage!")
        return opponent['magic']


main()