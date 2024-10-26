# 8-Puzzle Game Solver

This project implements a solution for the classic 8-puzzle game, where the goal is to rearrange tiles on a 3x3 grid to match a desired end configuration by moving tiles into a blank space. The solution utilizes a breadth-first search (BFS) algorithm to explore possible states and find the optimal solution, if one exists.

## Table of Contents
- About the Project
- Features
- Technologies Used
- Installation
- Usage
- Project Structure
- Examples
- License

## About the Project

The 8-puzzle game solver takes an initial puzzle state and attempts to find a series of moves that will transform it into a specified goal state. This project uses Python and `numpy` to handle state management and matrix manipulation for each move. The BFS algorithm ensures an efficient solution if one exists. 

## Features

- **Breadth-First Search (BFS)**: Finds the shortest sequence of moves to reach the goal.
- **State Management**: Tracks explored and frontier states to avoid redundant calculations.
- **Puzzle Validation**: Checks if a given puzzle configuration is solvable before attempting to solve.
- **Dynamic State Exploration**: Displays each move required to reach the solution.

## Technologies Used

- **Python**: Programming language used to develop the solver.
- **Numpy**: Library for efficient matrix operations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Juriez/8-Puzzle-Game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 8-Puzzle-Game
   ```
3. Install required dependencies:
   ```bash
   pip install numpy
   ```

## Usage

1. Run the script:
   ```bash
   python puzzle_solver.py
   ```
2. Input the initial state of the puzzle, row by row, as prompted. Represent the blank tile with a `0`.

3. The program will determine if the puzzle is solvable:
   - If **solvable**, the solution steps will be displayed.
   - If **unsolvable**, a message will indicate this.

### Example Input

```
Enter the initial state (3x3 grid) row by row, separated by spaces. Blank tile must be represented with 0.
Row 1: 1 2 3
Row 2: 4 0 5
Row 3: 6 7 8
```

## Project Structure

- **`puzzle_solver.py`**: Main program that includes classes for managing the puzzle state, solution search, and output display.
- **`README.md`**: Project documentation.

## Examples

Example Output:
```plaintext
Puzzle is solvable. Solving...
Initial State:
[[1 2 3]
 [4 0 5]
 [6 7 8]]

Expected State:
[[0 1 2]
 [3 4 5]
 [6 7 8]]

Solution Steps:

Move tile 4 down
[[0 2 3]
 [1 4 5]
 [6 7 8]]
...
Expected point reached in 6 actions!!
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

This README provides an overview of the 8-puzzle game solver, along with setup instructions and usage details. Feel free to add or modify sections as needed!
