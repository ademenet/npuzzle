import cython
import math
import numpy as np
cimport numpy as np
from utils import from_1d_to_2d


cdef find_coord(np.ndarray[np.int, ndim=1] state):
    """From 1D array return array of coordinates.

    It aims to return one array of coordinates to be used with np.unravel_index
    so as to use vectorized/no loop calculations.

    Example:
        state = [1, 3, 2, 4, 5, 6, 8, 7, 0]
        return [8, 0, 2, 1, 3, 4, 5, 7, 6]

    Args:
        state (np.ndarray) : 1D array of the state.

    Returns:
        (np.ndarray) Array of 1D coordinates.
    """
    cdef np.ndarray[np.int, ndim=1] arr_coord = np.empty(state.shape[0], dtype=np.int)
    for index in range(state.shape[0]):
        arr_coord[state[index]] = index
    return arr_coord


cpdef manhattan(np.ndarray[np.int, ndim=1] state, np.ndarray[np.int, ndim=1] goal, int size):
    """This is the Manhatthan heuristic.

    SUM(for i from 1 to s-1) : abs(Xgoal - Xstat_i) + abs(Ygoal - Ystat_i)

    Args:
        state (np.ndarray) : a puzzle state
        goal (np.ndarray) : the puzzle goal e.g final state
        s (int) : size of the puzzle

    Returns:
        heuristic value (int).
    """
    cdef int heur = 0
    cdef np.ndarray[np.int, ndim=1] coord_1d = find_coord(state)
    cdef np.ndarray[np.int, ndim=1] goal_coord_1d = find_coord(state)

    coord_2d = np.unravel_index(coord_1d, (size, size))
    # Passer les coord 2d de goal plutot que de recalculer a chaque fois
    goal_coord_2d = np.unravel_index(goal_coord_1d, (size, size))

    heur = np.sum(np.abs(goal_coord_2d[0] - coord_2d[0]) + np.abs(goal_coord_2d[1] - coord_2d[1]))

    return heur


cpdef euclidian_distance(np.ndarray[np.int, ndim=1] state, np.ndarray[np.int, ndim=1] goal, int size):
    """This is the euclidian distance heuristic.

        SUM(for i from 1 to s*s-1) : sqrt ((Xgoal - Xstat_i)^2 + (Ygoal - Ystat_i)^2)

        Args:
            state (int[]) : a puzzle state
            goal (int[]) : the puzzle goal e.g final state
            s (int) : size of the puzzle

        Returns:
            heuristic value (int).
    """
    cdef int heur = 0
    cdef np.ndarray[np.int, ndim=1] coord_1d = find_coord(state)
    cdef np.ndarray[np.int, ndim=1] goal_coord_1d = find_coord(state)

    coord_2d = np.unravel_index(coord_1d, (size, size))
    # Passer les coord 2d de goal plutot que de recalculer a chaque fois
    goal_coord_2d = np.unravel_index(goal_coord_1d, (size, size))

    heur = np.sum(np.sqrt(np.square(goal_coord_2d[0] - coord_2d[0]) + np.square(goal_coord_2d[1] - coord_2d[1])))

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
