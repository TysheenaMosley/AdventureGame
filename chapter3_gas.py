from utils import slow_print
from endings import safe_ending
from chapter4 import chapter4

def chapter3_gas(player):
    while True:
        slow_print("\nChapter 3: Gas Station")
        slow_print("Bright lights. Warm air.")
        slow_print("Safe... at least for now.")

        print("\n1. Ask the cashier for help")
        print("2. Stay inside")
        print("3. Buy charger")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            safe_ending(player)
            break
        elif choice == "2":
            chapter4(player)
            break
        elif choice == "3":
            player.add_item("charger")
            chapter4(player)
            break
        else:
            print("Invalid choice.")
