def isSolvable(puzzle):
	"""Check for each value wether the right hand values are inferior.
	If true, increment the 'inversion' variable for each superior right hand value found.
	"""
	inversion = 0
	for current in range(len(puzzle) - 1):
		for i in range(current + 1, len(puzzle)):
			if puzzle[current] > puzzle[i]:
				inversion += 1
	# It's solvable if the number of inversion is even
	return not inversion % 2
