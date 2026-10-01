def main_menu():
    choices = ["Start Game", "Credits", "Exit"]

    choices_number = 0
    print("===========================================")
    print("Choose one of the following options.")
    print("===========================================\n")

    for item in choices:
        choices_number += 1
        print(f"{choices_number}. {item}")

    choice = int(input("\nMake a choice: "))

    if choice == 1:
        start_game()
        
    elif choice == 2:
        credits()

    elif choice == 3:
        exit()

def start_game():
    start_room()
    hallway()

def start_room():
    has_key = False


    print("===========================================")
    print("You wake up in a dark room.")
    print("You see a desk, a small box and a door")
    print("===========================================\n")


    while True:
        

        choices = ["Check the desk", "Check the box", "Open the door", "Exit"]

        choices_number = 0

        for item in choices:
            choices_number += 1
            print(f"{choices_number}. {item}")

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

    print("===========================================")
    print("You walk over to the desk.")
    print("There is a letter for you on the desk.")
    print("===========================================")

    choice = input("Do you want to read the letter? (yes/no): ")

    if choice == "yes":
        pass
    else:
        print("You leave the letter alone.")


def check_box(has_key):

    print("You walk over to the box.")

    if has_key == True:
        print("The box is empty. You already took the key.")
        return has_key
 
     
    print("You see a key in the box.")

    choice = input("Do you want to take the key? (yes/no): ")

    if choice == "yes":
         has_key = True
         print("You take the key.")

    else:
        print("You leave the key in the box.")

    return has_key

# # Thomas


def open_door(has_key):

    print("You walk to the door.")

    choice = input("Do you want to open the door? (yes/no): ")

    if choice == "yes" and has_key == True:
        print("You open the door and enter the hallway.")
        return True

    elif choice == "yes":
        print("You dont have the key, go find it")
        return False

    else:
        print("You leave the door alone.")
        return False
# # Thomas

def hallway():

    print("===========================================")
    print("You enter the hallway.")
    print("There are 3 different door that you can choose from.")
    print("===========================================")

    while True:

        choices = ["First door", "Second door", "Third door", "Exit"]

        choices_number = 0

    
        for item in choices:
            choices_number += 1
            print(f"{choices_number}. {item}")

            choice = int(input("Choose a door: "))
        
            if choice == 1:
                First_door()
                
            elif choice == 2:
                Second_door()

            elif choice == 3:
                Third_door()


def First_door():
    print("===========================================")
    print("You open the first door.")
    print("Its a dark room that is faintly lit by candles.")
    print("You walk into the room")
    print("The door behind you suddenly locks")
    print("At the end of the room you see a corpse.")
    print("The corpse suddenly comes to life")
    print("===========================================")



def Second_door():
    print("You open the second door.")
    print("You walk into the room.")
    print("There is writing on the wall.")

    choice = input("Do you want to read the Writing on the wall? (yes/no): ")
    
    if choice == "yes":
        print("Sometimes the way forward is backwards.")
        print("476")

    else:
        print("You ignore the writing.")

def Third_door():
    print("You open the third door.")
    print("You walk into the room.")
    print("At the end of the room is a big door with some sort of lock.")
        
    choice = input("Do you want to inspect the lock? (yes/no): ")
    
    if choice == "yes":
        print("The lock needs a 3 digit code")

        code = input("enter the code: ")

        if code =="674":
            print("You hear a click.")
            print("The lock opens.")

        else:
            print("the code is incorrect.")

    else:
        print("You leave the lock alone.")
        






































































def credits(): 
    
    print("===========================================")
    print("Made by\n Mohamed Ali\n Thomas van Lingen")
    print("===========================================")


main_menu()