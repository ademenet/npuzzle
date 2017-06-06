import cython
import math
from utils import *

def find_coord(arr, int val, int s):
	"""Find the 2D coordinate of a value in a 1D array

	Args:
            arr (int[]) : 1D array
            val (int) : value to find
            s (int) : array size

        Returns:
            2D coordinates array [x,y]
	"""
	cdef int i = 0
	while arr[i] != val:
		i+=1
	return list(from_1d_to_2d(math.sqrt(s), i))

def distance_2_points(coord_ref, coord):

	return abs(coord_ref[0] - coord[0]) + abs(coord_ref[1] - coord[1])

def manhattan(state, goal, int s):
	"""This is the Manhatthan heuristic.

        SUM(for i from 1 to s-1) : abs(Xgoal - Xstat_i) + abs(Ygoal - Ystat_i)

        Args:
            state (int[]) : a puzzle state
            goal (int[]) : the puzzle goal e.g final state
            s (int) : size of the puzzle

        Returns:
            heuristic value (int).
	"""
	cdef int heur = 0
	cdef int i = 0
	s = s*s
	cdef int val
	for val in range(1, s):
		coord_ref = find_coord(goal, val, s)
		coord = find_coord(state, val, s)
		heur += distance_2_points(coord_ref, coord)
	return heur


def nSwap(state, goal, int s):
	"""n-Swap heuristic

        Represent the ‘space’ as a tile and assume you can swap any two tiles.

        Args:
            state (int[]) : a puzzle state
            goal (int[]) : the puzzle goal e.g final state
			s (int) : size of the puzzle

        Returns:
            heuristic value (int).
	"""
	cdef int heur = 0
	cdef int tile = 0
	cdef int ind_tmp
	cdef int tile_tmp
	while state != goal :
		if state.index(tile) != goal.index(tile):
			ind_tmp = state.index(tile)
			tile_tmp = state[goal.index(tile)]
			state[ind_tmp] = tile_tmp
			state[goal.index(tile)] = tile
			heur += 1
		tile += 1
		if tile > 8 : tile = 0
	return heur

def out_row_column(state, goal, int s):
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
	cdef int heur = 0
	for tile in range(1, s*s):
		coord = from_1d_to_2d(s, state.index(tile))
		coord_ref = from_1d_to_2d(s, goal.index(tile))
		if coord[0] != coord_ref[0]:heur += 1
		if coord[1] != coord_ref[1]:heur += 1
	return heur

def euclidian_distance(state, goal, int s):
	"""This is the euclidian distance heuristic.

        SUM(for i from 1 to s*s-1) : sqrt ((Xgoal - Xstat_i)^2 + abs(Ygoal - Ystat_i)^2)

        Args:
            state (int[]) : a puzzle state
            goal (int[]) : the puzzle goal e.g final state
            s (int) : size of the puzzle

        Returns:
            heuristic value (int).
	"""
	cdef int heur = 0
	cdef int i = 0
	cdef int n=s*s
	cdef int val
	for val in range(1, n):
		coord_ref = from_1d_to_2d(s,goal.index(val))
		coord = from_1d_to_2d(s,state.index(val))
		heur += math.sqrt((coord_ref[0] - coord[0])**2 + (coord_ref[1] - coord[1])**2)
	return heur
