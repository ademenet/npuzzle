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

def solve(start, end):
	neighbors = [-3, -1, 1, 3] # mouvements possibles
	open_set = [] # liste des 'routes' a explorer
	close_set = [] # liste des 'routes' explores et plus valable
	open_list = [] # liste des etats en cours
	heapq.heappush(open_set, start)
	heapq.heappush(open_list, start)
	# open_set.append((0, start)) # On ajoute le current dans la liste
	# open_list.append((0, start)) # on initialise ici aussi
	while open_set:
		current = heapq.heappop(open_list)
		if current == end:
			return retracePath(current)
		open_set.remove(current) # on retire de la liste a explorer et on met dans la liste exploree
		close_set.append(current)
		print("open_set 2 : %s" % open_set)
		print("close_set 2 : %s" % close_set)
		for tile in neighbors[current]: # on parcourt les possibilites
			if tile not in close_set: # si on est pas deja passe par la hop !
				# tile.H = manhattan(end.x, end.y, tile.x, tile.y)
				heuristic = abs(x_1 - x_2) + abs(y_1 - y_2) # calcul de l'heuristic
				if tile not in open_set: # si jamais explore, ajouter a la liste a explorer
					open_set.add(tile)
					heapq.heappush(open_list, (tile.H, tile)) # on fout tout avec lheuristic en classement
				tile.parent = current # plus on sauvegarde le parent
	return open_list

current = [1, 3, 2]
end = [1, 2, 3]
solve(neighbors, current, end)
