import sys
import random

while True:
    op = input("Attak or Defense: ")

    if op == "a" or op == "A":
        operator = random.randint(1,10)

        if operator == 1:
            print("Thatcher")
        elif operator == 2:
            print("Sledge")

        elif operator == 3:
            print("Ash")
        elif operator == 4:
            print("Thermite")

        elif operator == 5:
            print("Twitch")
        elif operator == 6:
            print("Montagne")

        elif operator == 7:
            print("Glaz")
        elif operator == 8:
            print("Fuze")

        elif operator == 9:
            print("Blitz")
        elif operator == 10:
            print("IQ")

        #elif operator == 11:
            #print("Buck")
        #elif operator == 12:
            #print("Blackbeard")
        #elif operator == 13:
            #print("Capitao")
        #elif operator == 14:
            #print("Hibana")
        #elif operator == 15:
            #print("Jackal")

    elif op == "d" or op == "D":
        operator = random.randint(20,29)

        if operator == 20:
            print("Smoke")
        elif operator == 21:
            print("Mute")

        elif operator == 22:
            print("Castle")
        elif operator == 23:
            print("Pulse")

        elif operator == 24:
            print("Doc")
        elif operator == 25:
            print("Rook")

        elif operator == 26:
            print("Kapkan")
        elif operator == 27:
            print("Tachanka")

        elif operator == 28:
            print("Jager")
        elif operator == 29:
            print("Bandit")

        #elif operator == 30:
            #print("Frost")
        #elif operator == 31:
            #print("Caveira")
        #elif operator == 32:
            #print("Echo")
        #elif operator == 33:
            #print("Mira")

    else:
        print("Noob, choose Recruit.")
