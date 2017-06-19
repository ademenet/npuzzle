import heapq
import cython
import numpy as np
from heuristic import manhattan
from debug import show_tree
from utils import *


class Node:
    """This class is used to store nodes informations and states.

    Args:
        state (1D numpy array): actual state of the node.
        parent (Node): parent state.
        cost (int): cost so far, cost of this actual node.
    """
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __eq__(self, other):
        """Compare only if state (1D numpy array) is equal to other."""
        return np.array_equal(self.state, other)

    def __hash__(self):
        return hash(tuple(self.state))

    def __lt__(self, other):
        return self.cost < other.cost


def _retracePath(state):
    """Display all the states from initial to goal.

    TODO: Finish"""
    while state is not None:
        print(state.state.reshape(3, 3))
        state = state.parent


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
    index_zero = np.argmin(current.state)
    i, j = from_1d_to_2d(size, index_zero)

    for index in neighbors:
        copy = np.copy(current.state)
        if 0 <= i + index[0] < size and 0 <= j + index[1] < size:
            to_switch_with = from_2d_to_1d(size, i + index[0], j + index[1])
            copy[index_zero] = current.state[to_switch_with]
            copy[to_switch_with] = 0
            neighbor = Node(state=copy, parent=current, cost=current.cost + 1)
            list_neighbor.append(neighbor)
    return list_neighbor


def solve(start, goal, size):
    """Solve the puzzle using A* algorithm.

    Args:
        start (1D numpy array): starting state.
        goal (1D numpy array): goal state.
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
    # Initialize a new Node
    start = Node(start)
    # Our two sets, it's easier to use sets than lists because of the hash, it
    # is only O(1) to find if a state is allready
    open_list = set()
    closed_list = set()
    # We still need a list to use as our binary min heap.
    heap = []
    heapq.heappush(heap, (start.cost, start))
    # Initialize the open list
    open_list.add(start)

    # Variables asked by the subject:
    stats = {'time_complexity': 1,  # Total number of states ever selected in open list
             'size_complexity': 0,  # Maximum number of states represented at the same time in lists
             'moves': 0}            # Number of moves required to transition from first state to goal state

    while open_list:
        current = heapq.heappop(heap)
        closed_list.add(current[1])
        if np.array_equal(current[1].state, goal):
            print("Reach the goal")
            print("Time complexity: ", stats['time_complexity'])
            stats['size_complexity'] = len(open_list) + len(closed_list)
            print("Size complexity: ", stats['size_complexity'])
            _retracePath(current[1])
            return
        open_list.remove(current[1])

        for state in _neighbors(size, current[1]):
            if state not in closed_list:
                heuristic = manhattan(current[1].state, goal, size)
                fn = state.cost + heuristic
                if state not in open_list:
                    open_list.add(state)
                    heapq.heappush(heap, (fn, state))

                    stats['time_complexity'] += 1
    return
