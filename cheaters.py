from lab68 import Player

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

class Smart_Cheat_Swapper(Player):
    def cheat(self):
        lostDie = min(self.dice)
        for x in range(len(self.dice)):
            if self.dice[x] == lostDie:
                self.dice[x] = 6
                break

class Cheat_Die_Flipper(Player):
    def cheat(self):
        for x in range(len(self.dice)):
            if self.dice[x] < 4:
                self.dice[x] = 7 - self.dice[x]


if __name__ == "__main__":
    cheater = Smart_Cheat_Swapper()
    cheater.roll()
    cheater.cheat()
