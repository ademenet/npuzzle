import numpy as np
import cython

def _get_index(int size, int i, int j):
	"""Get the index inside the spiral.

	In other words, we compute in which square belong the point of coordinates
	(i, j). It's 0 for the outer square, 1 one inner, 2 and therefore.
	For example, a 4*4 square:
		0 0 0 0
		0 1 1 0
		0 1 1 0
		0 0 0 0
	Args:
		size (int): puzzle size.
		i (int): coordinate.
		j (int): coordinate.
	Returns:
		square number (int) of the point belongs to.
	"""
	cdef int x
	cdef int y
	x = min(i, size - 1 - i)
	y = min(j, size - 1 - j)
	return min(x, y)

def _start_number(int size, int k):
	"""This functions returns the top left number (or the start number) of the
	square k. Start at 1."""
	return 4 * k * (size - k) + 1

def _get_number(int size, int i, int j):
	"""Description incoming!

	Args:
		size (int):
		i (int):
		j (int):

	Returns:
		number (int):
	"""
	cdef int k = _get_index(size, i, j)
	cdef int start = _start_number(size, k)
	cdef int offset = 0
	if i == k:
		offset += j - k
	else:
		offset += size - 1 - k - k
		if j == size - 1 - k:
			offset += i - k
		else:
			offset += size - 1 - k - k
			if i == size - 1 - k:
				offset += size - 1 - k - j
			else:
				offset += size - 1 - k - k
				offset += size - 1 - k - i
	return start + offset

def goal_generator(int size, int dim=1):
	"""This class generates the N-puzzle goal for the A star algorithm.

	Args:
		size (int): the size of the N-puzzle, should be > 2.
		dim (int): the dimension of your output, choose between 1 or 2
			dimensions.
	Returns:
		goal (array): the generated solution.
	"""
	goal = np.ndarray(size * size, dtype=np.uint64)
	if size < 3:
		raise Exception("Can't generate goal for puzzle lower than 2.")
	assert(dim == 1 or dim == 2), "Dimension should be 1 or 2."
	for i in range(size):
		for j in range(size):
			number = _get_number(size, i, j) if _get_number(size, i, j) != size * size else 0
			goal[i * size + j] = number
	if dim == 1:
		return goal
	else:
		return np.reshape(goal, (size, size))
