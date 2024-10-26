import numpy as np

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any((node.state[0] == state[0]).all() for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        node = self.frontier.pop()
        return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        node = self.frontier.pop(0)
        return node

class Puzzle:
    def __init__(self, start, start_index, goal, goal_index):
        self.start = [start, start_index]
        self.goal = [goal, goal_index]
        self.solution = None

    def neighbors(self, state):
        mat, (row, col) = state
        neighbors_list = []

        if row > 0:
            mat_copy = np.copy(mat)
            mat_copy[row][col] = mat_copy[row - 1][col]
            mat_copy[row - 1][col] = 0
            neighbors_list.append(('down', mat_copy[row - 1][col], [mat_copy, (row - 1, col)]))

        if col > 0:
            mat_copy = np.copy(mat)
            mat_copy[row][col] = mat_copy[row][col - 1]
            mat_copy[row][col - 1] = 0
            neighbors_list.append(('right', mat_copy[row][col - 1], [mat_copy, (row, col - 1)]))

        if row < 2:
            mat_copy = np.copy(mat)
            mat_copy[row][col] = mat_copy[row + 1][col]
            mat_copy[row + 1][col] = 0
            neighbors_list.append(('up', mat_copy[row + 1][col], [mat_copy, (row + 1, col)]))

        if col < 2:
            mat_copy = np.copy(mat)
            mat_copy[row][col] = mat_copy[row][col + 1]
            mat_copy[row][col + 1] = 0
            neighbors_list.append(('left', mat_copy[row][col + 1], [mat_copy, (row, col + 1)]))

        return neighbors_list

    def print_solution(self):
        if self.solution is None:
            print("No solution found.")
            return

        print(f"Initial State:\n{self.start[0]}\n")
        print(f"Expected State:\n{self.goal[0]}\n")
        print(f"\nStates Explored: {self.num_explored}\n")
        print("Solution Steps:\n")

        for action, tile, state in zip(*self.solution):
            print(f"Move tile {tile} {action}\n{state[0]}\n")
        print(f"Expected point reached in {len(self.solution[0])} actions!!")

    def does_not_contain_state(self, state):
        return all((st[0] != state[0]).any() for st in self.explored)

    def solve(self):
        self.num_explored = 0

        start_node = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start_node)

        self.explored = []

        while True:
            if frontier.empty():
                raise Exception("No solution")

            node = frontier.remove()
            self.num_explored += 1

            if (node.state[0] == self.goal[0]).all():
                actions, tiles, states = [], [], []
                while node.parent is not None:
                    actions.append(node.action)
                    moved_tile = node.parent.state[0][node.state[1]]
                    tiles.append(moved_tile)
                    states.append(node.state)
                    node = node.parent
                actions.reverse()
                tiles.reverse()
                states.reverse()
                self.solution = (actions, tiles, states)
                return

            self.explored.append(node.state)

            for action, tile, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and self.does_not_contain_state(state):
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

def get_puzzle_input():
    print("Enter the initial state (3x3 grid) row by row, separated by spaces. Blank tile must be represented with 0.")
    puzzle = []
    for i in range(3):
        row = input(f"Row {i + 1}: ").strip().split()
        puzzle.append([int(x) for x in row])

    puzzle = np.array(puzzle)
    blank_index = tuple(np.argwhere(puzzle == 0)[0])

    return puzzle, blank_index

def is_solvable(puzzle):
    flattened = puzzle.flatten()
    flattened = flattened[flattened != 0]
    inversions = sum(flattened[i] > flattened[j] for i in range(len(flattened)) for j in range(i + 1, len(flattened)))

    return inversions % 2 == 0

start, start_index = get_puzzle_input()
goal = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
goal_index = (0, 0)

if is_solvable(start):
    print("Puzzle is solvable. Solving...")
    puzzle = Puzzle(start, start_index, goal, goal_index)
    puzzle.solve()
    puzzle.print_solution()
else:
    print("This puzzle configuration is unsolvable, as the number of inversion point for this combination is odd")
