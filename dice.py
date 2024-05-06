# This python program resembles a dice, that is a dice simulator

import random 

COLS = 3
ROWS = 5

class Dice:


    @staticmethod       #staticmethod utilized because this program doesnot have any instances
    def get_side(side):     
           
        if side == 1:
            print("=========")
            print("|       |")
            print("|   o   |")
            print("|       |")
            print("=========")


        if side == 2:
            print("=========")
            print("|       |")
            print("| o   o |")
            print("|       |")
            print("=========")

        if side == 3:
            print("=========")
            print("|       |")
            print("| o o o |")
            print("|       |")
            print("=========")
        if side == 4:
            print("=========")
            print("| o   o |")
            print("|       |")
            print("| o   o |")
            print("=========")
        if side == 5:
            print("=========")
            print("| o   o |")
            print("|   o   |")
            print("| o   o |")
            print("=========")
        if side == 6:
            print("=========")
            print("| o o o |")
            print("|       |")
            print("| o o o |")
            print("=========")

            
        
def main():

    print("This program gives you the dice sumilation")
    ans = input("\nHit enter to continue and <q> to quit :")
    while ans != "q":
        num = random.randrange(1,7)

        # dices = Dice(num)
        Dice.get_side(num)     # calling the method without defining any instances

        # This is a sentinal loop

        ans = input("Hit enter to continue and <q> to quit :")


        ##This program can also do programmed without defining and new class and just use a new function or with in the main function with exactly same logic and functionality

main()