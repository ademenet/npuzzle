import heapq
import cython
import numpy as np
# from heuristic import manhattan
from debug import show_tree

# WIP

def retracePath(c):
    path = [c]
    while c.parent is not None:
        c = c.parent
        path.append(c)
    path.reverse()
    return path

# TODO ??? remplacer par une structure
# TODO recoder la fonction heappopm heappush et heapq ???

# neighbors renvoit les etats qui se trouvent apres l'etat envoye

def from_1d_to_2d(size, coord_1d):
	"""Convert 1D coordinates into 2D coordinates from 0 to size - for a square."""
	i = int(coord_1d / size)
	j = int(coord_1d % size)
	return i, j

def from_2d_to_1d(size, i, j):
	"""Convert 2D coordinates into 1D coordinates from 0 to (size - 1) - for a
	square."""
	return i * size + j

def neighbors(size, current):
	"""It returns new states from the current state given in argument using a
	yield generator."""
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
	""""""
	return np.sum(np.abs(np.subtract(current, goal)))

# TODO Garder les parents pour pouvoir afficher le chemin de la solution

def solve(start, goal, size):
	# Using set() instead of list is clever, because it's O(1) search time
	# whereas list are O(n). In fact, Python is using __hash__ object to
	# go faster. If you need documentation:
	# https://docs.python.org/3/reference/datamodel.html#object.__hash__
	# http://effbot.org/zone/python-hash.htm
	# https://en.wikipedia.org/wiki/Hash_tree
	# Thus we'll use these set in order to compare the current state with our
	# open list and closed list.
	open_list = set()
	closed_list = set()
	# We still need a list to initialize our binary min heap.
	heap = []
	heapq.heappush(heap, (0, start))
	open_list.add(tuple(start))
	print(np.reshape(start, (3,3)))
	while open_list:
		current = heapq.heappop(heap)
		closed_list.add(tuple(current[1]))
		print(current[1])
		if current[1] == goal:
			print("END!")
			return
			# return retracePath(current)
		open_list.remove(tuple(current[1]))
		closed_list.add(tuple(current[1]))
		for state in neighbors(size, current[1]): # on parcourt les possibilites
			if tuple(state) not in closed_list: # si on est pas deja passe par la hop !
				heuristic = manhattan(current[1], goal)
				# tile.H = manhattan(goal.x, goal.y, tile.x, tile.y)
				if tuple(state) not in open_list: # si jamais explore, ajouter a la liste a explorer
					open_list.add(tuple(state))
					heapq.heappush(heap, (heuristic.item(), state.tolist())) # on fout tout avec lheuristic en classement
				# tile.parent = current # plus on sauvegarde le parent
	return
# start = [1, 3, 2]
# end = [1, 2, 3]
# solve(neighbors, current, end)
# start = [6, 5, 4, 1, 0, 8, 7, 2, 3]
# start = [3,5,0,1,4,2,7,6,8]
# start = [5,3,7,1,6,2,0,8,4]
start = [8,1,7,5,4,6,2,3,0]

goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
solve(start, goal, 3)
