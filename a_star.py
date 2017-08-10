import heapq
import cython
import numpy as np
from heuristic import *
from debug import show_tree
from utils import *
from termcolor import colored, cprint
import time
import os
# from pqdict import minpq


class PriorityQueue():
    """Not thread-safe PriorityQueue implementation."""
    def __init__(self):
        self.queue = []

    def display(self):
        import copy
        heap = copy.copy(self.queue)
        while heap:
            print(heapq.heappop(heap))

    def put(self, priority, item):
        heapq.heappush(self.queue, (priority, item))

    def get(self):
        return heapq.heappop(self.queue)[1]

    def length(self):
        return len(self.queue)


def display(state, size):
    for i in range(size):
        for j in range(size):
            if state[i * size + j] == 0:
                cprint(state[i * size + j], 'red', end=' ')
            else:
                cprint(state[i * size + j], 'white', end=' ')
        print()
    print()


def _retracePath(came_from, current, stats, size):
    """Display all the states from initial to goal.

    Args:
        state (Node)
        stats (dict)
    """
    solution = []
    state = current
    print("Complexity in time: ", stats['time_complexity'])
    print("Complexity in size: ", stats['size_complexity'])
    while state is not None:
        solution.append(state)
        state = came_from[str(state)]
    print("Number of moves: ", len(solution) - 1)
    print("Solution:")
    for state in reversed(solution):
        display(state, size)


def _neighbors(size, current):
    """This generator returns new states from the current state given in argument.

    Args:
        size (int): square's size.
        current (Node): current state node.

    Return:
        list_neighbor (list of Node): returns a copy of the possible neighbor,
            corresponding to one potential move.
    """
    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    list_neighbor = []
    index_zero = np.argmin(current)
    i, j = from_1d_to_2d(size, index_zero)

    for index in neighbors:
        copy = np.copy(current)
        if 0 <= i + index[0] < size and 0 <= j + index[1] < size:
            to_switch_with = from_2d_to_1d(size, i + index[0], j + index[1])
            copy[index_zero] = current[to_switch_with]
            copy[to_switch_with] = 0
            neighbor = np.asarray(copy)
            list_neighbor.append(neighbor)
    return list_neighbor


def solve(start, goal, args):
    """Solve the puzzle using A* algorithm.

    Args:
        start (1D numpy array): starting state.
        goal (1D numpy array): goal state.
        args (dict): program args.

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

    came_from = {}
    g_score = {}
    f_score = {}
    size = args['size']
    heuristicFunction = getHeurstic(args['heuristic'])
    g = 1
    if args['greedy']:
        g = 0
    came_from[str(start)] = None
    g_score[str(start)] = 0
    f_score[str(start)] = heuristicFunction(start, goal, size)
    heap = PriorityQueue()
    heap.put(0, start.tolist())
    stats = {'time_complexity': 1,  # Total number of states ever selected in open list
             'size_complexity': 0,  # Maximum number of states represented at the same time in lists
             'moves': 0}            # Number of moves required to transition from first state to goal state
             
    while heap:
        current = np.asarray(heap.get())

        if np.array_equal(current, goal):
            _retracePath(came_from, current, stats, size)
            return

        for state in _neighbors(size, current):
            state_g_score = g_score[str(current)] + g
            if str(state) not in g_score or state_g_score < g_score[str(state)]:
                came_from[str(state)] = current

                g_score[str(state)] = state_g_score
                f_score[str(state)] = state_g_score + heuristicFunction(state, goal, size)

                heap.put(f_score[str(state)], state.tolist())
                stats['time_complexity'] += 1
                stats['size_complexity'] = max(stats['size_complexity'], heap.length())

    return
