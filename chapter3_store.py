from utils import slow_print
from endings import safe_ending
from chapter4 import chapter4

def chapter3_store(player):
    while True:
        slow_print("\nChapter 3: The Store")
        slow_print("Warm air hits instantly.")
        slow_print("For a moment, everything feels safe.")
        slow_print("The cashier looks over and can tell Jordan has been out in the cold too long.")

        print("\n1. Ask the cashier for help")
        print("2. Buy food and water")
        print("3. Leave quickly")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            safe_ending(player)
            break
        elif choice == "2":
            player.add_item("snack")
            player.add_item("water")
            chapter4(player)
            break
        elif choice == "3":
            chapter4(player)
            break
        else:
            print("Invalid choice.")
