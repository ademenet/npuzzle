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

def neighbors(current, size):
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
"""
def solve(start, end, size):
	open_set = () # tuple des 'routes' a explorer
	close_set = () # tuple des 'routes' explores et plus valable
	# open_list = [] # liste des etats en cours # test sans
	heapq.heappush(open_set, (0, start))
	# heapq.heappush(open_list, (0, start)) # test sans
	# open_set.append((0, start)) # On ajoute le current dans la liste
	# open_list.append((0, start)) # on initialise ici aussi
	while open_set:
		current = heapq.heappop(open_list)
		if current[1] == end:
			return retracePath(current)
		open_set.remove(current) # on retire de la liste a explorer et on met dans la liste exploree
		close_set.append(current)
		for index in neighbors[current]: # on parcourt les possibilites
			if tile not in close_set: # si on est pas deja passe par la hop !
				# tile.H = manhattan(end.x, end.y, tile.x, tile.y)
				heuristic = abs(x_1 - x_2) + abs(y_1 - y_2) # calcul de l'heuristic
				if tile not in open_set: # si jamais explore, ajouter a la liste a explorer
					open_set.add(tile)
					heapq.heappush(open_list, (tile.H, tile)) # on fout tout avec lheuristic en classement
				tile.parent = current # plus on sauvegarde le parent
	return open_list
"""
# start = [1, 3, 2]
# end = [1, 2, 3]
# solve(neighbors, current, end)
current = [4, 3, 5, 0, 1, 6, 2, 7, 8]
print(np.reshape(current, (3, 3)))
size = 3
for index in neighbors(current, size):
	# print (current)
	print (index)
	print (np.reshape(index, (3,3)))
# neighbors(current, size)
