import random 

COLS = 3
ROWS = 5

class Dice:

    def __init__(self,side):
        self.side = side

    @staticmethod
    def get_side(self):
           
        if self.side == 1:
            print("=========")
            print("|       |")
            print("|   o   |")
            print("|       |")
            print("=========")

        if self.side == 2:
            print("=========")
            print("|       |")
            print("| o   o |")
            print("|       |")
            print("=========")

        if self.side == 3:
            print("=========")
            print("|       |")
            print("| o o o |")
            print("|       |")
            print("=========")
        if self.side == 4:
            print("=========")
            print("| o   o |")
            print("|       |")
            print("| o   o |")
            print("=========")
        if self.side == 5:
            print("=========")
            print("| o   o |")
            print("|   o   |")
            print("| o   o |")
            print("=========")
        if self.side == 6:
            print("=========")
            print("| o o o |")
            print("|       |")
            print("| o o o |")
            print("=========")

            
        
def main():

    print("This program gives you the dice sumilation")
    ans = input("\nHit enter to continue and <q> to quit :")
    while ans != "q":
        num = 1
        # num = random.randrange(1,6)

        dices = Dice(num)
        dices.get_side()

        ans = input("Hit enter to continue and <q> to quit :")

main()