#import cython
from a_star import from_1d_to_2d

def find_coord(arr, val,s):
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
		i+=1
	return list(from_1d_to_2d(s, i))

def distance_2_points(coord_ref, coord):
	
	return abs(coord_ref[0] - coord[0]) + abs(coord_ref[1] - coord[1])

def manhattan (state, goal,s):
	"""This the Manhatthan implementation.

		SUM(for i from 1 to s-1) : abs(Xgoal - Xstat_i) + abs(Ygoal - Ystat_i)

		Args:
			state (int[]) : a puzzle state
			goal (int[]) : the puzzle goal e.g final state 
			s (int) : size of the puzzle

		Returns:
			heuristic value (int).   
	"""
	heur = 0
	i = 0
	coord_ref = []
	coord = []
	for val in range(1, s-1):
		coord_ref = find_coord(goal, val, s)
		coord = find_coord(state, val, s)
		heur += distance_2_points(coord_ref, coord)
	return heur
