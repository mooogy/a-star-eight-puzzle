from puzzle import Puzzle, get_valid_moves, expand
from search import manhattan_dist, informed_search

def main():
    p = Puzzle([1, 2, 3, 0, 4, 5, 7, 8, 6])
    informed_search(p)


    p = Puzzle([1, 2, 3, 0])
    informed_search(p)


if __name__ == '__main__':
    main()

