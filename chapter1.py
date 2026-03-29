import time
from utils import slow_print
from chapter2_main import chapter2_main
from chapter2_alley import chapter2_alley
from chapter2_call import chapter2_call

def chapter1(player):
    while True:
        slow_print("\nChapter 1: Leaving the Library")
        slow_print("Jordan steps outside and immediately feels the cold hit hard.")
        slow_print("Snow falls in thick sheets, covering everything in white.")
        slow_print("The last bus is gone.")
        time.sleep(1)
        slow_print("The campus is quiet... a little too quiet.")
        time.sleep(1)

        print("\n1. Walk down Main Street (lights)")
        print("2. Take the alley shortcut")
        print("3. Stay and call for help")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            player.gain_courage()
            chapter2_main(player)
            break
        elif choice == "2":
            player.lose_energy()
            chapter2_alley(player)
            break
        elif choice == "3":
            player.add_item("phone")
            chapter2_call(player)
            break
        else:
            print("Invalid choice.")
