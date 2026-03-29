import time
from utils import slow_print
from chapter3_low_battery import chapter3_low_battery
from chapter2_main import chapter2_main

def chapter2_call(player):
    while True:
        slow_print("\nChapter 2: No Answer")
        slow_print("Jordan calls...")
        time.sleep(1)
        slow_print("It rings.")
        time.sleep(1)
        slow_print("No answer.")
        slow_print("The cold is getting worse.")

        print("\n1. Wait longer")
        print("2. Start walking")
        print("3. Look for security")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            player.lose_energy()
            chapter3_low_battery(player)
            break
        elif choice == "2":
            chapter2_main(player)
            break
        elif choice == "3":
            player.gain_courage()
            chapter2_main(player)
            break
        else:
            print("Invalid choice.")
