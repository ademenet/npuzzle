import random
import numpy as np
from isSolvable import isSolvable


def puzzle_generator(size, goal):
    """Generate a random solvable n-puzzle.

    Args:
        size (int): size of the edge (not the total square).
        goal (1D numpy array): the goal to reach, e.g final puzzle state.

    Returns:
        npuzzle solvable (1D numpy array).
    """
    random.seed()
    limit = size * size
    while True:
        puzzle = [-1] * limit
        rdm = random.randrange(0, limit)
        for cnt in range(0, limit):
            while puzzle[rdm] != -1:
                rdm = random.randrange(0, limit)
            puzzle[rdm] = cnt
        puzzle = np.asarray(puzzle, dtype=int)
        if isSolvable(puzzle, goal, size):
            return puzzle

if __name__ == '__main__':
    from goal_generator import goal_generator
    import argparse
    parser = argparse.ArgumentParser(description="Generate puzzle on demand.")
    parser.add_argument('size', nargs='?', default=3, help="choose size for the puzzle")
    args = parser.parse_args()
    print(puzzle_generator(int(args.size), goal_generator(int(args.size), dim=1)))
