import cython
import numpy as np
cimport numpy as np
from utils import *

def inversion(puzzle):
	"""Check for each value wether the right hand values are inferior. If true,
	increment the 'inversion' variable for each superior right hand value found.

	Args:
		puzzle (1D numpy array): the puzzle to check, in is initial state form.
	"""
	cdef int inversion = 0
	cdef int current
	cdef int i
	for current in range(puzzle.size - 1):
		for i in range(current + 1, puzzle.shape[0]):
			if puzzle[current] > puzzle[i]:
				inversion += 1
	return inversion

def isSolvable(puzzle, goal, int size):
	"""Check if a uzzle is solvable.

	compare the polarity of the numbers of inversion between the puzzle and the goal

	Args:
		puzzle (1D numpy array): the puzzle to check, in is initial state form.
		goal (1D numpy array): the goal to reach, e.g final puzzle state
		size (int): puzzle width

	Returns:
		boolean: True if solvable, False if not.
	"""
	cdef int inversion_puzzle = inversion(puzzle)
	cdef int inversion_goal = inversion(goal)
	if (puzzle.size % 2 == 0):
		inversion_puzzle += (size - from_1d_to_2d(size, np.where(puzzle == 0)[0])[0]) % 2
		inversion_goal += (size - from_1d_to_2d(size, np.where(goal == 0)[0])[0]) % 2
		print (type(inversion_puzzle))
	if (inversion_puzzle % 2) == (inversion_goal % 2):
		return True
	else:
		return False
