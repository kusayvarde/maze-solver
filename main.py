import curses
import queue
import time
from curses import wrapper
import random

def generate_maze(row, col):
    maze = []
    border = []
    for i in range(row):
        maze_row = []
        for j in range(col):
            if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                maze_row.append("#")
                if i == j == 0 or (i == row - 1 and j == col - 1) or (i == 0 and j == col - 1) or (i == row - 1 and j == 0):
                    continue
                border.append((i, j))
            elif random.random() < 0.2:
                maze_row.append("#")
            else:
                maze_row.append(" ")
        maze.append(maze_row)
    
    start = random.choice(border)
    end = random.choice(border)
    maze[start[0]][start[1]] = "S"
    maze[end[0]][end[1]] = "E"
    return maze


def print_maze(maze, stdscr, path=[]):
    stdscr.clear()
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    GREEN = curses.color_pair(3)
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == "S":
                stdscr.addstr(i, j * 2, val, GREEN)
            elif val == "E":
                stdscr.addstr(i, j * 2, val, GREEN)
            elif (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, val, BLUE)
    stdscr.refresh()
                
                
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == start:
                return (i, j)
    return None

def find_path(maze, stdscr):
    start = "S"
    end = "E"
    start_pos = find_start(maze, start)
    
    
    q = queue.Queue()
    q.put((start_pos, [start_pos]))    
    
    visited = set()
    
    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        
        print_maze(maze, stdscr, path)
        
        if maze[row][col] == end:
            return path
        
        neighbours = find_neighbours(maze, current_pos)
        for neighbour in neighbours:
            if neighbour in visited:
                continue
        
            q.put((neighbour, path + [neighbour]))
            visited.add(neighbour)

        
def find_neighbours(maze, pos):    
    neighbours = []
    row, col = pos
    if row > 0 and maze[row - 1][col] != "#":
        neighbours.append((row - 1, col))
    if row < len(maze) - 1 and maze[row + 1][col] != "#":
        neighbours.append((row + 1, col))
    if col > 0 and maze[row][col - 1] != "#":
        neighbours.append((row, col - 1))
    if col < len(maze[0]) - 1 and maze[row][col + 1] != "#":
        neighbours.append((row, col + 1))
    return neighbours



def main(stdscr):
    max_y, max_x = stdscr.getmaxyx()
    
    BLUE = curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    RED = curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    GREEN = curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    maze = generate_maze(max_y - 2, max_x // 2)
    path = find_path(maze, stdscr)
    
    print_maze(maze, stdscr, path)
    stdscr.addstr("\nMaze solving completed in {} steps".format(len(path)))
    stdscr.refresh()
    
    stdscr.getch()
wrapper(main)
    