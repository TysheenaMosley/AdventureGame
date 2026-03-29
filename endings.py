import time
from utils import slow_print, show_status

def best_ending(player):
    slow_print("\nChapter 5: Best Ending")
    slow_print("Jordan keeps walking under the streetlights and finally makes it home safely.")
    slow_print("The walk was long and freezing, but trusting instinct made all the difference.")
    slow_print("Tonight taught Jordan that the safer choice is not always the easiest one.")

    if "charger" in player.items:
        slow_print("Having the charger helped Jordan feel a little more prepared.")
    if "water" in player.items:
        slow_print("The water helped Jordan push through the cold.")
    if "snack" in player.items:
        slow_print("The snack gave Jordan enough energy to keep going.")

    show_status(player)
    slow_print("THE END")

def safe_ending(player):
    slow_print("\nChapter 5: Safe Ending")
    slow_print("Jordan gets help from a worker inside and makes it home safely.")
    slow_print("Being careful about who to trust turned out to be the right move.")

    if "charger" in player.items:
        slow_print("The charger was a smart backup to have.")
    if "water" in player.items:
        slow_print("The water helped Jordan stay steady.")
    if "snack" in player.items:
        slow_print("The snack helped Jordan keep going.")

    show_status(player)
    slow_print("THE END")

def tired_ending(player):
    slow_print("\nChapter 5: Tired Ending")
    slow_print("Jordan makes it home... barely.")
    slow_print("The shortcut through the park led to a fall on the ice.")
    slow_print("Cold. Exhausted. Shaken.")
    slow_print("The faster choice turned out to be the harder one.")

    if "charger" in player.items:
        slow_print("At least the charger kept the phone alive.")
    if "water" in player.items:
        slow_print("The water helped a little on the way.")
    if "snack" in player.items:
        slow_print("The snack gave Jordan a small boost.")

    show_status(player)
    slow_print("THE END")

def stranger_ending(player):
    slow_print("\nChapter 5: Game Over")
    slow_print("Jordan finally asks the stranger at the bus stop for help.")
    time.sleep(1)
    slow_print("At first, the stranger sounds kind and concerned.")
    time.sleep(1)
    slow_print("But something starts to feel wrong.")
    time.sleep(1)
    slow_print("Before Jordan can get away, the situation turns dangerous.")
    time.sleep(1)
    slow_print("Jordan realizes too late that trusting the wrong person was the worst decision of the night.")
    show_status(player)
    slow_print("GAME OVER")
