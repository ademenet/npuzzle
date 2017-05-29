import random
from isSolvable import *

def puzzle_generator(s):
	"""Generate a random Solvable sPuzzle"""
	random.seed()
	while True :
		puzzle = [-1] * s
		rdm = random.randrange(0,s)
		for cnt in range (0,s):
			while (puzzle[rdm] != -1):
				rdm = random.randrange(0,s)
			puzzle[rdm] = cnt
		if isSolvable(puzzle):
			return puzzle

