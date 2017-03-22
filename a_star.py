import heapq
import cython
import numpy as np
from heuristic import manhattan
from debug import show_tree

# WIP

def retracePath(c):
    path = [c]
    while c.parent is not None:
        c = c.parent
        path.append(c)
    path.reverse()
    return path

def solve(graph, current, end):
	neighbors = [-3, -1, 1, 3]
	open_set = set()
	close_set = set()
	open_list = []
	open_set.add(current)
	open_list.append((0, current))
	while open_set:
		current = heapq.heappop(open_list)[1]
		if current == end:
			return retracePath(current)
		open_set.remove(current)
		close_set.add(current)
		for tile in graph[current]:
			if tile not in close_set:
				tile.H = manhattan(end.x, end.y, tile.x, tile.y)
				if tile not in open_set:
					open_set.add(tile)
					heapq.heappush(open_list, (tile.H, tile))
				tile.parent = current
	return open_list
