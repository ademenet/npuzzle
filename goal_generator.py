def _get_index(size, i, j):
	"""Get the index inside the spiral."""
	x = min(i, size - 1 - i)
	y = min(j, size - 1 - j)
	return min(x, y)

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
