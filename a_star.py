import heapq
import cython
import numpy as np
# from heuristic import manhattan
from debug import show_tree

# WIP

def retracePath(c):
	print("COUCOU")
	path = [c]
	while c.parent is not None:
	    c = c.parent
	    path.append(c)
	path.reverse()
	print(path)
    # return path

# TODO ??? remplacer par une structure
# TODO recoder la fonction heappopm heappush et heapq ???

# neighbors renvoit les etats qui se trouvent apres l'etat envoye

def from_1d_to_2d(size, coord_1d):
	"""Convert 1D coordinates into 2D coordinates from 0 to size - for a square.

	Args:
		size (int): square's size.
		coord_1d(int): 1 dimension coordinate.

	Returns:
		i, j (int, int): 2D coordinates with i (equivalent to x) and j (y).
	"""
	i = int(coord_1d / size)
	j = int(coord_1d % size)
	return i, j

def from_2d_to_1d(size, i, j):
	"""Convert 2D coordinates into 1D coordinates from 0 to (size - 1) - for a
	square.

	Args:
		size (int): square's size.
		i(int): x equivalent.
		j(int): y equivalent.

	Returns:
		coord_1d (int): 1D coordinates.
	"""
	return i * size + j

def neighbors(size, current):
	"""This generator eturns new states from the current state given in argument.

	Args:
		size (int): square's size.
		current (1D array): this is a current state contains into 1D array.

	Yields:
		copy (1D array): returns a copy of the possible neighbor, corresponding
			to one potential move.
	"""
	neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	index_zero = np.argmin(current)
	i, j = from_1d_to_2d(size, index_zero)
	for index in neighbors:
		copy = np.copy(current)
		if 0 <= i + index[0] < size and 0 <= j + index[1] < size:
			to_switch_with = from_2d_to_1d(size, i + index[0], j + index[1])
			copy[index_zero] = current[to_switch_with]
			copy[to_switch_with] = 0
			yield copy

def manhattan(current, goal):
	"""WIP this manhattant implementation is SOOOO wrong!"""
	return np.sum(np.abs(np.subtract(current, goal)))

# TODO Garder les parents pour pouvoir afficher le chemin de la solution

def solve(start, goal, size):
	"""Solve the puzzle using A* algorithm.

	Args:
		start (1D array): starting state.
		goal (1D array): goal state.
		size (int): square's size.

	Returns:

	Using set() instead of list is clever, because it's O(1) search time
	whereas list are O(n). In fact, Python is using __hash__ object to
	go faster. If you need documentation:

		https://docs.python.org/3/reference/datamodel.html#object.__hash__
		http://effbot.org/zone/python-hash.htm
		https://en.wikipedia.org/wiki/Hash_tree

	Thus we'll use these set in order to compare the current state with our
	open list and closed list. It optimizes the accessibility, instead of
	looking into the heap to know if we have allready explored one state.
	"""
	# Our two sets, it's easier to use sets than lists because of the hash, it
	# is only O(1) to find if a state is allready
	open_list = set()
	closed_list = set()
	# We still need a list to use as our binary min heap.
	heap = []
	heapq.heappush(heap, (0, start))
	parent = {}

	open_list.add(tuple(start))

	while open_list:
		current = heapq.heappop(heap)

		closed_list.add(tuple(current[1]))

		if current[1] == goal:
			print("END!")
			return retracePath(closed_list)

		# print("current: {}".format(current))
		open_list.remove(tuple(current[1]))


		# closed_list.add(tuple(current[1]))
		for state in neighbors(size, current[1]): # on parcourt les possibilites
			if tuple(state) not in closed_list: # si on est pas deja passe par la hop !
				heuristic = manhattan(current[1], goal)
				# tile.H = manhattan(goal.x, goal.y, tile.x, tile.y)
				if tuple(state) not in open_list: # si jamais explore, ajouter a la liste a explorer

					open_list.add(tuple(state))

					heapq.heappush(heap, (heuristic.item(), state.tolist())) # on fout tout avec lheuristic en classement
					# TESTING
					# parent.add(tuple((tuple(state), tuple(current[1]))))
				# tile.parent = current # plus on sauvegarde le parent
	return
