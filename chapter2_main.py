from utils import slow_print
from chapter3_store import chapter3_store
from chapter3_bus import chapter3_bus

def chapter2_main(player):
    while True:
        slow_print("\nChapter 2: Main Street")
        slow_print("Jordan walks under the streetlights.")
        slow_print("Snow keeps falling, heavier now.")
        slow_print("Up ahead, a small store is still open.")
        slow_print("Across the street, someone is standing near the bus stop.")

        print("\n1. Go into the store")
        print("2. Keep walking")
        print("3. Cross the street")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            player.gain_courage()
            chapter3_store(player)
            break
        elif choice == "2":
            player.lose_energy()
            chapter3_bus(player)
            break
        elif choice == "3":
            player.gain_courage()
            chapter3_bus(player)
            break
        else:
            print("Invalid choice.")
