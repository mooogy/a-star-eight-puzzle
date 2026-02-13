# Unimportant typing information support
from __future__ import annotations
from collections.abc import Callable

# Original subroutine
from puzzle import Puzzle, expand

# Unoriginal subroutine
from heapq import heappop, heappush

# Node class for search
class Node():
    depth: int
    cost: int
    puzzle: Puzzle

    def __init__(self, depth: int, cost: int, puzzle: Puzzle):
        self.depth = depth
        self.cost = cost
        self.puzzle = puzzle
    
    # Equality and less than operations for heapq subroutine support
    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.depth + self.cost == other.depth + other.cost

    def __lt__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.depth + self.cost < other.depth + other.cost


# Helper function to easily calculate manhattan distance
def index_to_grid(index: int, size: int):
    row = index // size
    col = index % size

    return row, col

# Manhattan distance heuristic
def manhattan_dist(p: Puzzle):
    total_dist = 0

    for i, tile in enumerate(p.state):
        if tile == i + 1 or tile == 0: continue

        curr_row, curr_col = index_to_grid(i, p.size)
        goal_row, goal_col = index_to_grid(tile - 1, p.size)
        
        total_dist += (abs(curr_row - goal_row) + abs(curr_col - goal_col))

    return total_dist

# A* implementation with custom heuristic as a parameter (If None, then its just Uniform Cost Search since h(x) = 0)
def A_star(initial_puzzle: Puzzle, heuristic: Callable[Puzzle] = None):
    # Establish goal state for a n x n puzzle
    goal = list(range(1, initial_puzzle.size**2)) + [0]
    
    # Create queue with initial state as the only node
    queue = [Node(0, 0, initial_puzzle)]
    
    # Breaks when goal state is found or no solution is found
    while True:
        if len(queue) == 0:
            print('FAILURE\n')
            break

        node = heappop(queue)
        if node.puzzle.state == goal:
            print('SUCCESS\n')
            break

        new_puzzles = expand(node.puzzle)

        for puz in new_puzzles:
            # If no heuristic is used, h(x) = 0
            cost = 0 if heuristic == None else heuristic(puz)
            heappush(queue, Node(node.depth + 1, cost, puz))
    
    print(node.puzzle)
    print(f'Final Node Depth: {node.depth}, Cost: {node.cost}')

