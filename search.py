from __future__ import annotations
from dataclasses import dataclass
from puzzle import Puzzle, expand
from heapq import heappop, heappush
from functools import total_ordering

def index_to_grid(index: int, size: int):
    row = index // size
    col = index % size

    return row, col

def manhattan_dist(p: Puzzle):
    total_dist = 0

    for i, tile in enumerate(p.state):
        if tile == i + 1 or tile == 0: continue

        curr_row, curr_col = index_to_grid(i, p.size)
        goal_row, goal_col = index_to_grid(tile - 1, p.size)
        
        total_dist += (abs(curr_row - goal_row) + abs(curr_col - goal_col))

    return total_dist

def informed_search(p: Puzzle):
    goal = list(range(1,p.size**2)) + [0]

    queue = [Node(0, 0, p)]

    while True:
        if len(queue) == 0:
            print('FAILURE\n')
            break

        node = heappop(queue)

        print(node.puzzle, end='')
        print(f'Node cost: {node.depth + node.cost}\n')

        if node.puzzle.state == goal:
            print('SUCCESS\n')
            break

        new_puzzles = expand(node.puzzle)

        for puz in new_puzzles:
            cost = manhattan_dist(puz)
            heappush(queue, Node(node.depth + 1, cost, puz))

@dataclass
@total_ordering
class Node():
    depth: int
    cost: int
    puzzle: Puzzle

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.depth + self.cost == other.depth + other.cost

    def __lt__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.depth + self.cost < other.depth + other.cost
