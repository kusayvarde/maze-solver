# Maze Solver

This project is a terminal-based maze generator and solver built using Python's `curses` library. It generates a random maze, finds the shortest path from the start (`S`) to the end (`E`), and visualizes the solution in the terminal.

## Features

- Random maze generation with walls (`#`), open paths (` `), start (`S`), and end (`E`) points.
- Visualization of the maze and the solving process in the terminal.
- Uses breadth-first search (BFS) to find the shortest path.
- Color-coded display:
  - **Blue**: Walls and open paths.
  - **Green**: Start (`S`) and end (`E`) points.
  - **Red**: Path taken to solve the maze.

## How to Run

1. Clone this repository or download the `main.py` file.
2. Ensure you have Python installed on your system.
3. Run the script using the following command:

   ```bash
   python main.py
   ```

4. The maze will be displayed in the terminal, and the solving process will be visualized step by step.

## Requirements

- Python 3.x
- `curses` library (pre-installed with Python on most systems)

## How It Works

1. **Maze Generation**: 
   - The maze is generated with random walls and open paths.
   - The start (`S`) and end (`E`) points are placed on the border of the maze.

2. **Pathfinding**:
   - The program uses breadth-first search (BFS) to find the shortest path from `S` to `E`.
   - The solving process is visualized in real-time.

3. **Visualization**:
   - The maze is displayed in the terminal with color-coded elements.
   - The path is marked with `X` as the solver progresses.


## Customization

- You can modify the maze size by adjusting the terminal window size.
- The density of walls can be changed by modifying the probability in the `generate_maze` function.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Built using Python's `curses` library for terminal-based UI.
- Inspired by classic maze-solving algorithms.
