# Original subroutines
from puzzle import Puzzle
from search import A_star, manhattan_dist

def main():
    p = Puzzle([1, 2, 3, 0, 4, 5, 7, 8, 6])
    print(p)
    A_star(p)

    p = Puzzle([0, 2, 3, 1])
    print(p)
    A_star(p)

if __name__ == '__main__':
    main()

