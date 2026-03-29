from utils import slow_print
from endings import best_ending, tired_ending, safe_ending

def chapter4(player):
    while True:
        slow_print("\nChapter 4: The Final Stretch")
        slow_print("Jordan is close now.")
        slow_print("But it's darker... quieter... colder.")

        print("\n1. Stay under the lights")
        print("2. Cut through the park")
        print("3. Knock on a nearby door")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            best_ending(player)
            break
        elif choice == "2":
            player.lose_energy()
            tired_ending(player)
            break
        elif choice == "3":
            safe_ending(player)
            break
        else:
            print("Invalid choice.")
