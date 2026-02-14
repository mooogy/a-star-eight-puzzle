# Original subroutines
from puzzle import Puzzle
from search import A_star, manhattan_dist, misplaced_tile

def set_custom_puzzle() -> Puzzle:
    PUZZLE_SIZE_MESSAGE = (
                '\nHow big would you like your n x n puzzle to be? (integers >= 2 only!)\n'
            )
    print(PUZZLE_SIZE_MESSAGE)
    size = int(input('n = '))

    if size < 2:
        raise ValueError('Custom puzzle size is less than minimum!')

    PUZZLE_INPUT_INSTRUCTIONS = (
                '\nYou will now be asked to input your puzzle row by row.\n'
                f'For each row, please input {size} numbers separated by spaces.\n'
                'Please represent the blank (empty) tile with a 0.\n'

                '\nSimple 2x2 example:\n'
                '1 0\n'
                '3 2\n'
            )
    print(PUZZLE_INPUT_INSTRUCTIONS)
    
    puzzle_state = []
    for i, row in enumerate(range(size)):
        input_row = input(f'Row {i + 1}: ')
        
        row_state = []
        for num in input_row.split(' '):
            row_state.append(int(num))
        
        puzzle_state.extend(row_state)

    return Puzzle(puzzle_state)

# Main program
def main() -> None:
    WELCOME_MESSAGE = (
                'Welcome to the n-puzzle solver!\n\n'
                'To begin, please select an algorithm to solve with:\n'
                '\t1) Uniform Cost Search\n'
                '\t2) A* (Misplaced Tile Heuristic)\n'
                '\t3) A* (Manhattan Distance Heuristic)\n'
            )
    print(WELCOME_MESSAGE)
    
    algo_map = {'1': None, '2': misplaced_tile, '3': manhattan_dist}
    algorithm_choice = input('(1 / 2 / 3): ')

    if algorithm_choice in algo_map:
        algorithm = algo_map[algorithm_choice] 
    
    PUZZLE_INPUT_MESSAGE = (
                '\nHow would you like to set the puzzle?:\n'
                '\t1) I would like to enter my own n x n puzzle!\n'
                '\t2) I would like to use a default 3x3 puzzle.\n'
            )
    print(PUZZLE_INPUT_MESSAGE)
    puzzle_input_choice = input('(1 / 2): ')

    # Depth 11 default 3x3 puzzle
    puzzle = Puzzle([
            2, 3, 5,
            0, 8, 4,
            1, 7, 6
        ])

    if puzzle_input_choice == '1':
        puzzle = set_custom_puzzle()

    SHOW_NODES_MESSAGE = (
                '\nLastly, would you like to see node information for nodes visited by the search?\n'
                '(This could generate a wall of text and increase the time taken by the algorithm!)\n'
                '\t1) No, just solve it already!\n'
                '\t2) Yes, show me the nodes!\n'
            )
    print(SHOW_NODES_MESSAGE)
    show_nodes = True if input('(1 / 2): ') == '2' else False

    A_star(puzzle, algorithm, show_nodes)

if __name__ == '__main__':
    main()

