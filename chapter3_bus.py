from utils import slow_print
from endings import stranger_ending
from chapter4 import chapter4

def chapter3_bus(player):
    while True:
        slow_print("\nChapter 3: Bus Stop")
        slow_print("Jordan reaches the bus stop and stands under the shelter.")
        slow_print("Snow blows in from the sides, and the bench is covered in ice.")
        slow_print("A stranger nearby notices Jordan shivering and starts asking questions.")
        slow_print("The stranger says they can help.")

        print("\n1. Keep walking")
        print("2. Ask the stranger for help")
        print("3. Sit and rest")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            chapter4(player)
            break
        elif choice == "2":
            stranger_ending(player)
            break
        elif choice == "3":
            player.lose_energy()
            chapter4(player)
            break
        else:
            print("Invalid choice.")
