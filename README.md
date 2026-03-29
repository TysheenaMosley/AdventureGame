Adventure Game: The Long Walk Home
Author: Tysheena Mosley
Course: CSS-225
Date: March 2026

--------------------------------------------------

OVERVIEW:
This is a text-based adventure game where the player controls Jordan, who must make decisions to safely get home on a cold winter night. Each choice affects the outcome of the story and leads to different endings.

--------------------------------------------------

WHERE THE CODE IS HOSTED:
The code is hosted on GitHub (link provided separately).

--------------------------------------------------

LANGUAGES AND TECHNOLOGIES:
- Python 3
- Python IDLE (used for development)

--------------------------------------------------

SYSTEM REQUIREMENTS:
- Python 3 installed
- Works in any Python environment (IDLE, terminal, etc.)

--------------------------------------------------

FILE STRUCTURE:
The game is split into multiple Python files:
- main.py (starts the game)
- player.py (Player class)
- utils.py (printing and helper functions)
- chapter files (game logic)
- endings.py (game endings)

This structure makes the program modular and easier to maintain.

--------------------------------------------------

HOW TO RUN THE GAME:
1. Open main.py
2. Press F5 in IDLE
3. Follow the on-screen instructions

--------------------------------------------------

HOW THE GAME WORKS:
The game is divided into chapters. Each chapter is stored in a separate Python file. The player makes choices that determine which path the story follows.

The Player class tracks:
- Energy
- Courage
- Items

Different choices lead to different endings:
- Safe Ending
- Best Ending
- Tired Ending
- Game Over (bad decisions)

--------------------------------------------------

ARCHITECTURE OVERVIEW:
The game uses modular programming. Each chapter is a separate file and is imported into other files as needed. The main.py file acts as the entry point.

--------------------------------------------------

ERROR HANDLING:
Invalid inputs are handled by prompting the user to re-enter their choice.
