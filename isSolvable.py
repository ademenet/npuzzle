# Check for each value wether the right hand values are superior.
#  If true, increment the 'inversion' variable for each superior right hand value.

def isSolvable(puzzle):
	inversion = 0
	for current in range(len(puzzle) - 1):
		for i in range(current + 1, len(puzzle)):
			if puzzle[current] > puzzle[i]:
				inversion += 1
	# Is solvable is the number of inversion is even
	return not inversion % 2
