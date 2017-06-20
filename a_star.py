import heapq
import cython
import numpy as np
from heuristic import manhattan
from debug import show_tree
from utils import *


class PriorityQueue():
    """Not thread-safe PriorityQueue implementation."""
    def __init__(self):
        self.queue = []

    def put(self, priority, item):
        heapq.heappush(self.queue, (priority, item))

    def get(self):
        return heapq.heappop(self.queue)[1]

    def length(self):
        return len(self.queue)


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

    # def __eq__(self, other):
    #     """Compare only if state (1D numpy array) is equal to other."""
    #     return np.array_equal(self.state, other)

    # def __hash__(self):
        # return hash(tuple(self.state))

    def __lt__(self, other):
        return self.cost < other.cost

    def key(self):
        return (str(self.state))

def _retracePath(state, stats):
    """Display all the states from initial to goal.

    Args:
        state (Node)
        stats (dict)
    """
    solution = []
    print("Complexity in time: ", stats['time_complexity'])
    print("Complexity in size: ", stats['size_complexity'])
    while state is not None:
        solution.insert(0, state.state)
        state = state.parent
    print("Number of moves: ", len(solution) - 1)
    print("Solution:")
    for state in solution:
        print(state)


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
    # open_list = set()
    # closed_list = set()

    open_list = {}
    closed_list = {}

    heap = PriorityQueue()
    heap.put(start.cost, start)

    # Initialize the open list
    # open_list.add(start)
    open_list[start.key()] = start

    # Variables asked by the subject:
    stats = {'time_complexity': 1,  # Total number of states ever selected in open list
             'size_complexity': 0,  # Maximum number of states represented at the same time in lists
             'moves': 0}            # Number of moves required to transition from first state to goal state

    while open_list:
        current = heap.get()
        # closed_list.add(current)

        if np.array_equal(current.state, goal):
            _retracePath(current, stats)
            return

        del open_list[current.key()]
        closed_list[current.key()] = current

        # open_list.remove(current)
        # print(open_list)
        # open_list.pop(current.key())

        for state in _neighbors(size, current):
            # if (state.key() in closed_list and state.cost >= closed_list[state.key()].cost) or (state.key() in open_list and state.cost >= open_list[state.key()].cost):
                # continue
            # else:
            if state.key() in closed_list:
                continue
            if state.key() in open_list:
                if state.cost < current.cost:
                    current = state
            # if state.key() not in open_list or state.cost < open_list[state.key()].cost:
            else:
                heuristic = manhattan(current.state, goal, size)
                # print("heuristic: {}, cost: {}".format(heuristic, state.cost))
                fn = state.cost + heuristic
                # if state.cost >=
                # open_list.add(state)
                open_list[state.key()] = state
                heap.put(fn, state)
            # print("open_list: ", open_list)
        # input()

    return
