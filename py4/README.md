# Memory Tile Game

## Overview
This is a simple command-line based memory tile game where players uncover pairs of tiles to match the symbols hidden beneath. The objective is to find all matching pairs by remembering the positions of the tiles. It is a fun and challenging way to test your memory skills.

## Game Setup
The game board comes in various sizes, based on difficulty level:
- Easy: 2x2 grid
- Medium: 4x4 grid
- Hard: 6x6 grid
- Extreme: 8x8 grid

### Rules:
1. At the start of the game, all tiles are hidden.
2. You will be prompted to uncover two tiles at a time.
3. Enter the coordinates of the tile you want to uncover. For example, `A0` will uncover the tile in row `A` and column `0`.
4. If the two uncovered tiles match, they will stay uncovered, and you proceed.
5. If the tiles don’t match, they will be hidden again.
6. The game continues until all pairs are matched.

## How to Play

1. **Start the game**: When you run the script, you'll be asked to choose a difficulty level:
   - Enter `EASY` for a 2x2 board.
   - Enter `MEDIUM` for a 4x4 board.
   - Enter `HARD` for a 6x6 board.
   - Enter `EXTREME` for an 8x8 board.

2. **Uncover a tile**: 
   - When prompted, enter the position of a tile using the letter for the row and number for the column.
   - For example, to uncover the tile at row `A` and column `0`, you would enter `A0`.
   
3. **Matching pairs**:
   - If you successfully uncover a pair of matching tiles, they remain visible.
   - If they don’t match, the tiles will be hidden again.

4. **Win condition**:
   - The game ends when all tiles are uncovered and matched.
   - The game will notify you of your victory once all pairs are found.

5. **Replay**:
   - After completing a round, you can choose to play again by typing `y` or exit by typing `n`.

## Example of Gameplay

Here is an example of the initial game board (2x2 grid):

   0         1     
|---------|---------| A | | | |---------|---------| B | | | |---------|---------|


**Enter the tile to uncover:**
- If you type `A0`, the tile at the first row and first column will be uncovered.

If the uncovered tile shows a letter (e.g., `G`), you need to find another tile with the same letter.

## How to Run the Game

1. Ensure you have Python installed on your system.
2. Copy the game code into a Python script (e.g., `memory_game.py`).
3. Run the game from the terminal or command prompt using:
   ```bash
   python memory_game.py

Dependencies
Python 3.x
No external libraries are required.
Future Improvements
Implement a timer to track how long the player takes to complete the game.
Add a scoring system based on the number of moves made.
Improve the user interface by adding colors to tiles.
