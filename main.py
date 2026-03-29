# ----------------------------------------------------------
# Adventure Game: The Long Walk Home
# Author: Tysheena Mosley
# Date: March 2026
# Course: CSS-225
# Final Version
# ----------------------------------------------------------

import time
from player import Player
from utils import slow_print
from chapter1 import chapter1

def main():
    slow_print("Welcome to The Long Walk Home")
    time.sleep(1)
    player = Player()
    chapter1(player)

main()
