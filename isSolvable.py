import numpy as np

def _unrollPuzzle(puzzle, size):
	"""Transform 1D array puzzle to an unroll puzzle to test solvability.

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
	"""
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
	return unroll

def isSolvable(puzzle, size):
	"""Check for each value wether the right hand values are inferior. If true,
	increment the 'inversion' variable for each superior right hand value found.

	Args:
		puzzle (1D numpy array): the puzzle to check, in is initial state form.

	Returns:
		boolean: True if solvable, False if not.
	"""
	puzzle = _unrollPuzzle(puzzle)
	inversion = 0
	for current in range(len(puzzle) - 1):
		for i in range(current + 1, len(puzzle)):
			if puzzle[current] > puzzle[i]:
				inversion += 1
	# It's solvable if the number of inversion is even
	return not inversion % 2
