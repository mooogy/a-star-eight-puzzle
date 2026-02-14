# Unimportant typing information support
from __future__ import annotations
from collections.abc import Callable

# Original subroutine
from puzzle import Puzzle, expand

# Unoriginal subroutine
from heapq import heappop, heappush
from time import perf_counter_ns

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
def index_to_grid(index: int, size: int) -> tuple[int, int]:
    row = index // size
    col = index % size

    return row, col

# Misplaced tile heuristic
def misplaced_tile(p: Puzzle) -> int:
    goal = list(range(1, p.size**2)) + [0]
    misplaced_count = 0

    for current, true in zip(p.state, goal):
        if current != 0 and current != true:
            misplaced_count += 1

    return misplaced_count


# Manhattan distance heuristic
def manhattan_dist(p: Puzzle) -> int:
    total_dist = 0

    for i, tile in enumerate(p.state):
        if tile == i + 1 or tile == 0: continue

        curr_row, curr_col = index_to_grid(i, p.size)
        goal_row, goal_col = index_to_grid(tile - 1, p.size)
        
        total_dist += (abs(curr_row - goal_row) + abs(curr_col - goal_col))

    return total_dist

# A* implementation with custom heuristic as a parameter (If None, then its just Uniform Cost Search since h(x) = 0)
# Returns diagnostics for analysis
def A_star(initial_puzzle: Puzzle, heuristic: Callable[[Puzzle], int] | None = None, show_nodes: bool = False, quiet: bool = False) -> tuple[int, int, int, int]:
    if not quiet: print('\nSOLVING...\n')
    
    # Timing for measurements
    start_time = perf_counter_ns()

    # Establish goal state for a n x n puzzle
    goal = list(range(1, initial_puzzle.size**2)) + [0]
    
    # Create queue with initial state as the only node
    queue = [Node(0, 0, initial_puzzle)]
    
    nodes_expanded = 0
    max_queue_size = 0

    visited = set()

    # Breaks when goal state is found or no solution is found
    while True:
        if len(queue) == 0:
            if not quiet: print('NO SOLUTION POSSIBLE')
            break

        max_queue_size = max(len(queue), max_queue_size)

        node = heappop(queue)
        state_str = "".join(map(str, node.puzzle.state))
        
        if state_str in visited:
            continue
        visited.add(state_str)

        if show_nodes:
            print(f'g(x): {node.depth} | h(x): {node.cost}')
            print(node.puzzle)

        if node.puzzle.state == goal:
            if not quiet: print('SOLUTION FOUND')
            break

        new_puzzles = expand(node.puzzle)
        nodes_expanded += 1

        for puz in new_puzzles:
            # If no heuristic is used, h(x) = 0
            cost = 0 if heuristic == None else heuristic(puz)
            heappush(queue, Node(node.depth + 1, cost, puz))

    end_time = perf_counter_ns()
    TIME_IN_MS = (end_time - start_time) / 1_000_000
    
    SUMMARY_MESSAGE = (
                '\nSEARCH SUMMARY\n'
                f'Highest Amount Of Nodes In Queue: {max_queue_size}\n'
                f'Total Nodes Expanded: {nodes_expanded}\n'
                f'Final Node Depth: {node.depth}\n'
                f'Time Elapsed: {TIME_IN_MS:.2f} ms'
            )
    if not quiet: print(SUMMARY_MESSAGE)

    return (nodes_expanded, max_queue_size, node.depth, TIME_IN_MS)
