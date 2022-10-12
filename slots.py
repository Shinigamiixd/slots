from random import randint
import sys
from time import sleep
from os import system
from subprocess import run

def slots():

    bet_amount = 100

    slots_selection = ["♠", "♥", "♦", "♣"]
    slots_row_1_col_1 = slots_selection[randint(0, 3)]
    slots_row_1_col_2 = slots_selection[randint(0, 3)]
    slots_row_1_col_3 = slots_selection[randint(0, 3)]
    
    slots_row_2_col_1 = slots_selection[randint(0, 3)]
    slots_row_2_col_2 = slots_selection[randint(0, 3)]
    slots_row_2_col_3 = slots_selection[randint(0, 3)]

    slots_row_3_col_1 = slots_selection[randint(0, 3)]
    slots_row_3_col_2 = slots_selection[randint(0, 3)]
    slots_row_3_col_3 = slots_selection[randint(0, 3)]

    system("cls")
    print(f"|   |   |   |")
    print(f"|   |   |   |")
    print(f"|   |   |   |")
    sleep(0.5)
    system("cls")

    print(f"| {slots_row_1_col_1} | {slots_row_1_col_2} | {slots_row_1_col_3} |")
    print(f"|   |   |   |")
    print(f"|   |   |   |")
    sleep(0.6)
    system("cls")

    print(f"| {slots_row_1_col_1} | {slots_row_1_col_2} | {slots_row_1_col_3} |")
    print(f"| {slots_row_2_col_1} | {slots_row_2_col_2} | {slots_row_2_col_3} |")
    print(f"|   |   |   |")
    sleep(0.7)
    system("cls")

    print(f"| {slots_row_1_col_1} | {slots_row_1_col_2} | {slots_row_1_col_3} |")
    print(f"| {slots_row_2_col_1} | {slots_row_2_col_2} | {slots_row_2_col_3} |")
    print(f"| {slots_row_3_col_1} | {slots_row_3_col_2} | {slots_row_3_col_3} |\n")

    if slots_row_1_col_1 == slots_row_1_col_2 == slots_row_1_col_3:
        # 1 1 1
        # 0 0 0
        # 0 0 0
        bet_amount *= 3
        print(f"You won ${bet_amount}")

    elif slots_row_2_col_1 == slots_row_2_col_2 == slots_row_2_col_3:
        # 0 0 0
        # 1 1 1
        # 0 0 0
        bet_amount *= 3
        print(f"You won ${bet_amount}")

    elif slots_row_3_col_1 == slots_row_3_col_2 == slots_row_3_col_3:
        # 0 0 0
        # 0 0 0
        # 1 1 1
        bet_amount *= 3
        print(f"You won ${bet_amount}")

    elif slots_row_1_col_1 == slots_row_1_col_2 == slots_row_1_col_3 == slots_row_2_col_1 == slots_row_2_col_2 == slots_row_2_col_3:
        # 1 1 1
        # 1 1 1
        # 0 0 0
        bet_amount *= 40
        print(f"You won ${bet_amount}")

    elif slots_row_2_col_1 == slots_row_2_col_2 == slots_row_2_col_3 == slots_row_3_col_1 == slots_row_3_col_2 == slots_row_3_col_3:
        # 0 0 0
        # 1 1 1
        # 1 1 1
        bet_amount *= 40
        print(f"You won ${bet_amount}")

    elif slots_row_1_col_1 == slots_row_1_col_2 == slots_row_1_col_3 == slots_row_2_col_1 == slots_row_2_col_2 == slots_row_2_col_3 == slots_row_3_col_1 == slots_row_3_col_2 == slots_row_3_col_3:
        # 1 1 1
        # 1 1 1
        # 1 1 1
        bet_amount *= 120
        print(f"You won ${bet_amount}")


slots()
input("Press ENTER to exit.")