import random
import os
from enemies import Ghost_knight, Mini_boss
from player import get_health, get_damage, take_damage

def main_menu():
    os.system("cls")
    choices = ["Start Game", "Credits", "Exit"]

    choices_number = 0
    print("===========================================")
    print("▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █ \n▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █ \n░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒\n░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒\n░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░\n ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ \n ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░\n ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░ \n   ░       ░              ░       ░    ░  ░    ░ ░           ░ \n ░")
    print("===========================================")
    print("Choose one of the following options.")
    print("===========================================\n")

    for item in choices:
        choices_number += 1
        print(f"{choices_number}. {item}")

    print("===========================================")

    choice = int(input("\nMake a choice: "))

    if choice == 1:
        start_game()
        
    elif choice == 2:
        credits()

    elif choice == 3:
        exit()

def start_game():
    os.system("cls")
    start_room()
    hallway()

def credits():
    os.system("cls")

    print("===========================================")
    print("                  CREDITS")
    print("===========================================")
    print()
    print("                Made by:")
    print("             Mohamed Ali")
    print("          Thomas van Lingen")
    print()
    print("===========================================")

def start_room():
    os.system("cls")
    has_key = False

    print("===========================================")
    print("               THE DARK ROOM")
    print("===========================================")
    print("You wake up in a dark room.")
    print("You see a desk, a small box and a door.")
    print("===========================================\n")

    while True:
        
        choices = ["Check the desk", "Check the box", "Open the door", "Exit"]

        choices_number = 0

        for item in choices:
            choices_number += 1
            print(f"{choices_number}. {item}")

        print("-------------------------------------------")

        choice = int(input("Make a choice: "))

        if choice == 1:
            check_desk()

        elif choice == 2:
            has_key = check_box(has_key)

        elif choice == 3:
            door_opened = open_door(has_key)

            if door_opened == True:
                return

        elif choice == 4:
            return

def check_desk():
    os.system("cls")

    print("===========================================")
    print("                 THE DESK")
    print("===========================================")
    print("You walk over to the desk.")
    print("There is a letter for you on the desk.")
    print("===========================================")

    choice = input("Do you want to read the letter? (yes/no): ")

    if choice == "yes":
        print("Dit is een demo")
    else:
        print("You leave the letter alone.")

def check_box(has_key):
    os.system("cls")

    print("===========================================")
    print("                  THE BOX")
    print("===========================================")
    print("You walk over to the box.")

    if has_key == True:
        print("The box is empty. You already took the key.")
        print("===========================================")
        return has_key
 
    print("You see a key in the box.")

    choice = input("Do you want to take the key? (yes/no): ")

    if choice == "yes":
         has_key = True
         print("You take the key.")

    else:
        print("You leave the key in the box.")

    print("===========================================")

    return has_key

# # Thomas

def open_door(has_key):
    os.system("cls")

    print("===========================================")
    print("                 THE DOOR")
    print("===========================================")
    print("You walk to the door.")

    choice = input("Do you want to open the door? (yes/no): ")

    if choice == "yes" and has_key == True:
        print("You open the door and enter the hallway.")
        print("===========================================")
        return True

    elif choice == "yes":
        print("You dont have the key, go find it.")
        print("===========================================")
        return False

    else:
        print("You leave the door alone.")
        print("===========================================")
        return False

# # Thomas

def hallway():
    os.system("cls")

    print("===========================================")
    print("                  HALLWAY")
    print("===========================================")
    print("You enter the hallway.")
    print("There are 3 different doors that you can choose from.")
    print("===========================================\n")

    while True:

        choices = ["First door", "Second door", "Third door", "Exit"]

        choices_number = 0
    
        for item in choices:
            choices_number += 1
            print(f"{choices_number}. {item}")

        print("-------------------------------------------")

        choice = int(input("Choose a door: "))
        
        if choice == 1:
            First_door()
                
        elif choice == 2:
            Second_door()

        elif choice == 3:
            Third_door()

def First_door():
    os.system("cls")

    print("===========================================")
    print("              THE FIRST DOOR")
    print("===========================================")
    print("You open the first door.")
    print("Its a dark room that is faintly lit by candles.")
    print("You walk into the room.")
    print("The door behind you suddenly locks.")
    print("At the end of the room you see a corpse.")
    print("The corpse suddenly comes to life!")
    print("===========================================")

    knight_health, knight_damage = Ghost_knight()

    while knight_health > 0:

        print("-------------------------------------------")
        print("                 COMBAT")
        print("-------------------------------------------")
        print(f"Your health:         {get_health()}")
        print(f"Ghost Knight health: {knight_health}")
        print("-------------------------------------------")
        print("1. Attack")
        print("2. Run")
        print("-------------------------------------------")

        choice = input("Choose: ")

        if choice == "1":
            knight_health -= get_damage()

            print("\nYou attack the Ghost Knight!")

            if knight_health <= 0:
                print("===========================================")
                print("       YOU DEFEATED THE GHOST KNIGHT!")
                print("===========================================")
                break

            take_damage(knight_damage)
 
            print("The Ghost Knight attacks you!")

        elif choice == "2":
            print("You cannot escape!")
        
def Second_door():
    os.system("cls")

    print("===========================================")
    print("              THE SECOND DOOR")
    print("===========================================")
    print("You open the second door.")
    print("You walk into the room.")
    print("There is writing on the wall.")
    print("===========================================")

    choice = input("Do you want to read the writing? (yes/no): ")
    
    if choice == "yes":
        print("-------------------------------------------")
        print("Sometimes the way forward is backwards.")
        print()
        print("                    476")
        print("-------------------------------------------")

    else:
        print("You ignore the writing.")

def Third_door():
    os.system("cls")

    print("===========================================")
    print("               THE THIRD DOOR")
    print("===========================================")
    print("You open the third door.")
    print("You walk into the room.")
    print("At the end of the room is a big door with some sort of lock.")
    print("===========================================")
        
    choice = input("Do you want to inspect the lock? (yes/no): ")
    
    if choice == "yes":
        print("-------------------------------------------")
        print("The lock needs a 3 digit code.")
        print("-------------------------------------------")

        code = input("Enter the code: ")

        if code == "674":
            print("You hear a click.")
            print("The lock opens.")

            mini_boss()

        else:
            print("The code is incorrect.")

    else:
        print("You leave the lock alone.")
        
def mini_boss():
    os.system("cls")

    print("===========================================")
    print("                 MINI BOSS")
    print("===========================================")
    print("You enter a large room.")
    print("The door slams shut behind you.")
    print("Something is waiting for you...")
    print("===========================================")

    boss_health, boss_damage = Mini_boss()

    while boss_health > 0:

        print("-------------------------------------------")
        print("                 COMBAT")
        print("-------------------------------------------")
        print(f"Your health:      {get_health()}")
        print(f"Mini Boss health: {boss_health}")
        print("-------------------------------------------")
        print("1. Attack")
        print("2. Run")
        print("-------------------------------------------")

        choice = input("Choose: ")

        if choice == "1":
            boss_health -= get_damage()

            print("\nYou attack the Mini Boss!")

            if boss_health <= 0:
                print("===========================================")
                print("         YOU DEFEATED THE MINI BOSS!")
                print("===========================================")
                break

            take_damage(boss_damage)

            print("The Mini Boss attacks you!")

        elif choice == "2":
            print("You cannot escape!")

main_menu()