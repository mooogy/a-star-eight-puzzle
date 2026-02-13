# Unimportant typing information support
from __future__ import annotations

# Unoriginal subroutine
from math import isqrt

class Puzzle():
    def __init__(self, state: list[int]):
        self.state = state
        self.size = isqrt(len(state))
        
        # Avoids any invalid non n x n 8-puzzles
        if self.size**2 != len(state):
            raise ValueError('Grid is not square! (n x n)')

        self.blank_index = state.index(0)
    
    # Represent method for print debugging
    def __repr__(self):
        puzzleString = ''
        for row in range(self.size):
            for col in range(self.size):
                index = col + (row*self.size)
                puzzleString += (str(self.state[index]) + ' ')
            puzzleString += '\n'
        return puzzleString

# Helper function to determine which moves are possible in a given puzzle state
def get_valid_moves(p: Puzzle) -> list[int]:
    m = p.size
    index = p.blank_index

    blank_row = index // m
    blank_col = index % m

    valid_moves = []
    
    # UP AND DOWN
    if blank_row > 0:
        valid_moves.append(index - m)
    if blank_row < (m-1):
        valid_moves.append(index + m)
    
    # LEFT AND RIGHT
    if blank_col > 0:
        valid_moves.append(index - 1)
    if blank_col < (m-1):
        valid_moves.append(index + 1)

    return valid_moves

# Expand puzzle to return a list of possible states that stem from the input puzzle
def expand(p: Puzzle) -> list[Puzzle]:
    moves = get_valid_moves(p)
    index = p.blank_index

    new_puzzles = []

    for move in moves:
        # Create new state with the blank moved
        next_state = p.state.copy()
        next_state[index], next_state[move] = next_state[move], next_state[index]

        new_puzzles.append(Puzzle(next_state))

    return new_puzzles

