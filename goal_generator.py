def _get_index(size, i, j):
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
	x = min(i, size - 1 - i)
	y = min(j, size - 1 - j)
	return min(x, y)

def _start_number(size, k):
	"""This functions returns the top left number (or the start number) of the
	square k."""
	return 4 * k * (size - k) + 1

def goal_generator(size, dim=1):
	"""This class generates the N-puzzle goal for the A star algorithm.

	Args:
		size (int): the size of the N-puzzle, should be > 2.
		dim (int): the dimension of your output, choose between 1 or 2
			dimensions.
	Returns:
		goal (array): the generated solution.
	"""
	if size < 3:
		raise Exception("Can't generate goal for puzzle lower than 2.")
	assert(dim == 1 or dim == 2), "Dimension should be 1 or 2."
	
