import cython
import numpy as np
import heapq
from goal_generator import goal_generator

# TODO implementer 3 heuristiques qui ont du sens
# TODO implementer le A*
# TODO implementer la gestion de heap ? Priority Queue ? Heapq ?
# TODO tester les performances a chaque fois

import time

def main():
	start = time.time()
	result = goal_generator(5)
	end = time.time()
	print(result)
	print("total time exec: {}".format(end - start))

if __name__ == '__main__':
	main()
