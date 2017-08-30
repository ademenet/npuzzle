import numpy as np
from utils import from_1d_to_2d


def inversion(puzzle):
    """Check for each value wether the right hand values are inferior. If true,
    increment the 'inversion' variable for each superior right hand value found.

    Args:
        puzzle (1D numpy array): the puzzle to check, in is initial state form.

    Returns:
        int: number of inversions.
    """
    inversions = 0
    N = puzzle.size - 1
    D = puzzle.shape[0]
    for current in range(N):
        for i in range(current + 1, D):
            if puzzle[current] > puzzle[i] and (puzzle[current] != 0 and puzzle[i] != 0):
                inversions += 1
    return inversions


def isSolvable(puzzle, goal, size):
    """Check if a puzzle is solvable.

    Compare the polarity of the numbers of inversion between the puzzle and the
    goal.

    Args:
        puzzle (1D numpy array): the puzzle to check, in is initial state form.
        goal (1D numpy array): the goal to reach, e.g final puzzle state
        size (int): puzzle width

    Returns:
        boolean: True if solvable, False if not.
    """
    inversion_puzzle = inversion(puzzle)
    inversion_goal = inversion(goal)
    if puzzle.size % 2 == 0:
        inversion_puzzle += (size - from_1d_to_2d(size, np.where(puzzle == 0)[0])[0]) % 2
        inversion_goal += (size - from_1d_to_2d(size, np.where(goal == 0)[0])[0]) % 2
    return inversion_puzzle % 2 == inversion_goal % 2
