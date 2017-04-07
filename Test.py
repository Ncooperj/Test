import sys
import random

while True:
    op = input("Attak or Defense: ")

    if op == "a" or op == "A":
        operator = random.randint(1,2)

        if operator == 1:
            print("Glaz")

        elif operator == 2:
            print("Sledge")

    elif op == "d" or op == "D":
        operator = random.randint(3,7)

        if operator == 3:
            print("Smoke")

        elif operator == 4:
            print("Twitch")

        elif operator == 5:
            print("Jager")

        elif operator == 6:
            print("Mira")

        elif operator == 7:
            print("Rook")

    else:
        print("Noob, choose Tachanka.")
