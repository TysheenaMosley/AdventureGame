from utils import slow_print
from chapter2_main import chapter2_main
from chapter4 import chapter4

def chapter3_low_battery(player):
    while True:
        slow_print("\nChapter 3: Low Battery")
        slow_print("2% battery.")
        slow_print("The phone flickers.")

        print("\n1. Save battery")
        print("2. Use flashlight")
        print("3. Make last call")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            chapter2_main(player)
            break
        elif choice == "2":
            player.lose_energy()
            chapter4(player)
            break
        elif choice == "3":
            player.gain_courage()
            chapter2_main(player)
            break
        else:
            print("Invalid choice.")
