# Java_Project_TicTacToe  
An Automated Tic-Tac-Toe Game with Adaptive Difficulty Modes

---

## PURPOSE AND PROBLEM BEING SOLVED

Standard text-based Tic-Tac-Toe games are often predictable, either allowing the player to win easily or forcing a tie every time. This project elevates the classic game by introducing dynamic AI difficulty layers to create a genuinely engaging challenge. 

- **Static Opponents**: Standard games rely on fixed patterns that players memorize quickly.  
- **Lack of Tension**: Traditional games fail to provide an aggressive opponent strategy.  
- **User Customization**: Most basic console games do not offer any game-mode selection.  

This Python project solves these issues by featuring an automated computer opponent that strategically claims the high-value center tile on turn one, and offers a specialized "Hard Mode" that bends the traditional rules to put the player on the defensive.

It improves console game interactivity, introduces robust input validation, and showcases randomized AI pathing.

---

## FEATURES

### Easy Mode
- Computer follows traditional rules and places exactly one 'X' per turn.
- Player places an 'O' per turn.
- Purely turn-based, standard competitive pacing.

### Hard Mode (Computer Advantage)
- The computer receives a special strategic advantage.
- The computer is granted the ability to place two 'X's during one of its turns.
- Drastically increases difficulty and forces the player to play defensively.

### System Features
- **Smart Opener**: Computer automatically secures the high-value center tile `board[1][1]` instantly on startup.
- **Input Validation**: Rejects inputs outside the 1-9 range and blocks players from overwriting already occupied spaces.
- **Dynamic Board Tracking**: Real-time evaluation of free spaces and automated lookups across 8 distinct winning combinations.
- **Console Interface**: Clean, text-based grid visualizer that updates instantly after every valid move.

---

## INSTRUCTIONS ON HOW TO RUN

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd /Users/albinda/Java_Project_TicTacToe
   ```
3. Run the Python file directly using:
   ```bash
   python3 MLabProject_Albinda_Megrino.py
   ```

---

## CORE SYSTEM ARCHITECTURE & CODE LOGIC

The script operates using a programmatic flow to handle board management, AI selection, and victory evaluations:

### 1. Board Representation & Win Tracking
- **`board`**: A two-dimensional list (matrix) serving as the grid coordinate system.
- **`winner`**: A static data list storing all 8 possible winning combinations (3 rows, 3 columns, 2 diagonals) used to continuously scan the grid state.

### 2. Primary Functions
- **`free(board)`**: Scans the matrix and compiles a clean list of all coordinates that do not currently contain an 'X' or 'O'.
- **`gold(board, player)`**: Cross-references the current grid with the `winner` matrix list to see if the specified player token has successfully chained 3 symbols together.
- **`board_open(board)`**: The rendering engine that prints the updated visual state of the grid to the console.
- **`randrange()`**: Sourced from Python's native `random` module to allow the AI to select an unexpected path out of the remaining `free()` spaces.

### 3. Game Loop Flow
- **Initialization**: Sets the center position `board[1][1] = "X"` automatically before opening inputs.
- **Turn Validation**: Evaluates user inputs against `"123456789"`. If a space is taken or invalid, it throws an error and loops back until a clean coordinate is given.
- **Evaluation Loop**: Alternates turns, checking `if gold(board, "O")` or `if gold(board, "X")` matches a win condition, or flags a tie if `len(free(board)) == 0`.

---

## GROUP MEMBERS & PRESENTATION NOTES
- **Princess Grace Albinda**  
- **Anthony John Megrino**  
