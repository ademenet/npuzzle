import cython
import numpy as np
cimport numpy as np
from utils import *

"""def _unrollPuzzle(puzzle, size):
	Transform 1D array puzzle to an unroll puzzle to test solvability.

	For example:
		5 8 2
		3 0 6
		4 7 1
	Gives us in 1D: 5 8 2 3 0 6 4 7 1
	And `_unrollPuzzle` will transform it to: 5 8 2 6 1 7 4 3 0

	Args:
		puzzle (1D numpy array): the puzzle to unroll.

	Returns:
		unrolled puzzle (1D numpy array)
	
	limit = size * size
	puzzle = np.reshape(puzzle, [size, size])
	unroll = np.zeros(size * size, dtype=int)
	t = 0   			# top
	l = 0   			# left
	b = puzzle.shape[0] - 1 # bottom
	r = puzzle.shape[1] - 1 # right
	i = 0               # iterator
	while i < limit:
		for col in range(l, r + 1, 1):
			unroll[i] = puzzle[t][col]
			i += 1
		t += 1
		if t > b: break
		for row in range(t, b + 1, 1):
			unroll[i] = puzzle[row][r]
			i += 1
		r -= 1
		if r < l: break
		for col in range(r, l - 1, -1):
			unroll[i] = puzzle[b][col]
			i += 1
		b -= 1
		if b < t: break
		for row in range(b, t - 1, -1):
			unroll[i] = puzzle[row][l]
			i += 1
		l += 1
		if l > r: break
	return unroll"""

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
