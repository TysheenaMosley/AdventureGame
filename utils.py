import time
import sys

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_status(player):
    slow_print("\n--- STATUS ---")
    slow_print(f"Energy: {player.energy}")
    slow_print(f"Courage: {player.courage}")
    slow_print(f"Items: {player.items if player.items else 'None'}")
    slow_print("----------------\n")
