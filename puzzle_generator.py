import random
from isSolvable import *
import numpy as np

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
	while True :
		puzzle = [-1] * limit
		rdm = random.randrange(0, limit)
		for cnt in range (0, limit):
			while (puzzle[rdm] != -1):
				rdm = random.randrange(0, limit)
			puzzle[rdm] = cnt
		puzzle = np.asarray(puzzle, dtype=int)
		if isSolvable(puzzle, goal, size):
			return puzzle
