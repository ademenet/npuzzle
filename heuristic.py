import math
import numpy as np
from utils import from_1d_to_2d


def find_coord(arr, val, s):
    """Find the 2D coordinate of a value in a 1D array

    Args:
        arr (int[]) : 1D array
        val (int) : value to find
        s (int) : array size

    Returns:
        2D coordinates array [x,y]
    """
    i = 0
    while arr[i] != val:
        i += 1
    return list(from_1d_to_2d(math.sqrt(s), i))


def distance_2_points(coord_ref, coord):
    return abs(coord_ref[0] - coord[0]) + abs(coord_ref[1] - coord[1])


def manhattan(state, goal, s):
    """This is the Manhatthan heuristic.

    SUM(for i from 1 to s-1) : abs(Xgoal - Xstat_i) + abs(Ygoal - Ystat_i)

    Args:
        state (int[]) : a puzzle state
        goal (int[]) : the puzzle goal e.g final state
        s (int) : size of the puzzle

    Returns:
        heuristic value (int).
    """
    heur = 0
    s = s * s
    for val in range(1, s):
        coord_ref = find_coord(goal, val, s)
        coord = find_coord(state, val, s)
        heur += distance_2_points(coord_ref, coord)
    return heur


def nSwap(state, goal, s):
    """n-Swap heuristic.

    Represent the ‘space’ as a tile and assume you can swap any two tiles.

    Args:
        state (int[]) : a puzzle state
        goal (int[]) : the puzzle goal e.g final state
        s (int) : size of the puzzle

    Returns:
        heuristic value (int).
    """
    heur = 0
    tile = 0
    tmpState = np.copy(state)
    while not np.array_equal(tmpState, goal):
        if np.where(tmpState==tile)[0][0] != np.where(goal==tile)[0][0]:
            ind_tmp = np.where(tmpState==tile)[0][0]
            tile_tmp = tmpState[np.where(goal==tile)[0][0]]
            tmpState[ind_tmp] = tile_tmp
            tmpState[np.where(goal==tile)[0][0]] = tile
            heur += 1
        tile += 1
        if tile > s**2 - 1:
            tile = 0
    return heur


def out_row_column(state, goal, s):
    """"out of row out of column heuristic

        Number of tiles out of row + Number of tiles out of
        column

        Args:
            state (int[]) : a puzzle state
            goal (int[]) : the puzzle goal e.g final state
            s (int) : size of the puzzle

        Returns:
            heuristic value (int).
    """
    heur = 0
    for tile in range(1, s*s):
        coord = from_1d_to_2d(s, np.where(state==tile)[0][0])
        coord_ref = from_1d_to_2d(s, np.where(goal==tile)[0][0])
        if coord[0] != coord_ref[0]:
            heur += 1
        if coord[1] != coord_ref[1]:
            heur += 1
    return heur


def euclidian_distance(state, goal, s):
    """This is the euclidian distance heuristic.

        SUM(for i from 1 to s*s-1) : sqrt ((Xgoal - Xstat_i)^2 + abs(Ygoal - Ystat_i)^2)

        Args:
            state (int[]) : a puzzle state
            goal (int[]) : the puzzle goal e.g final state
            s (int) : size of the puzzle

        Returns:
            heuristic value (int).
    """
    heur = 0
    n = s * s
    for val in range(1, n):
        coord_ref = from_1d_to_2d(s, np.where(goal==val)[0][0])
        coord = from_1d_to_2d(s, np.where(state==val)[0][0])
        heur += math.sqrt((coord_ref[0] - coord[0])**2 + (coord_ref[1] - coord[1])**2)
    return heur

def breadth(state, goal, s):
    """Breadth search is a particular case of A-star algorithm. It only takes in
    account the cost so far. Thus the 'breadth' heuristic always return 0."""
    return 0

def getHeurstic(heur):
    """Generate dict of available heuristics and returns one.

    Args:
        heur (str): heuristic choosen.

    Returns:
        the choosen heuristic function if success, manhattan otherwise.
    """
    dictHeur = {}
    dictHeur['manhattan distance'] = manhattan
    dictHeur['nSwap'] = nSwap
    dictHeur['euclidian distance'] = euclidian_distance
    dictHeur['out row column'] = out_row_column
    dictHeur['breadth'] = breadth

    if heur not in dictHeur:
        heur = 'manhattan distance'

    return dictHeur[heur]
