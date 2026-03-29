import time
from utils import slow_print
from chapter3_gas import chapter3_gas
from chapter3_bus import chapter3_bus
from chapter2_main import chapter2_main

def chapter2_alley(player):
    while True:
        slow_print("\nChapter 2: The Alley")
        slow_print("Jordan turns into the alley.")
        slow_print("The light disappears behind.")
        time.sleep(1)
        slow_print("Crunch... crunch... footsteps echo.")
        time.sleep(1)
        slow_print("Someone is behind.")

        print("\n1. Run")
        print("2. Hide")
        print("3. Go back")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            player.gain_courage()
            chapter3_gas(player)
            break
        elif choice == "2":
            player.lose_energy()
            chapter3_bus(player)
            break
        elif choice == "3":
            player.gain_courage()
            chapter2_main(player)
            break
        else:
            print("Invalid choice.")
