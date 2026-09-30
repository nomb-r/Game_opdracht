def main_menu():
    choices = ["Start Game", "Credits", "Exit"]

    choices_number = 0
    print("===========================================")
    print("Choose one of the following options")
    print("===========================================\n")

    for item in choices:
        choices_number += 1
        print(f"{choices_number}. {item}")

    choice = int(input("\nMake a choice: "))

    if choice == 1:
        start_room()
        

    elif choice == 2:
        pass

    elif choice == 3:
        pass


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
            pass

        elif choice == 3:
            pass

        elif choice == 4:
            pass


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

# def check_box():
#     print("You walk over to the box")

# # Thomas


# def open_door():

# # Thomas










def credits(): 
    
    print("===========================================")
    print("Made by\n Mohamed Ali\n Thomas van Lingen")
    print("===========================================")


main_menu()