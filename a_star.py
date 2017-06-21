import heapq
import cython
import numpy as np
from heuristic import manhattan
from debug import show_tree
from utils import *
from termcolor import colored, cprint
from pqdict import minpq


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
    print("Number of moves: ", len(came_from) - 1)
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
    # index_zero = np.argmin(current.state)
    i, j = from_1d_to_2d(size, index_zero)

    for index in neighbors:
        copy = np.copy(current)
        # copy = np.copy(current.state)
        if 0 <= i + index[0] < size and 0 <= j + index[1] < size:
            to_switch_with = from_2d_to_1d(size, i + index[0], j + index[1])
            copy[index_zero] = current[to_switch_with]
            # copy[index_zero] = current.state[to_switch_with]
            copy[to_switch_with] = 0
            # neighbor = Node(state=copy, parent=current, cost=current.cost + 1)
            neighbor = np.asarray(copy)
            list_neighbor.append(neighbor)
    return list_neighbor


# def astar(start, goal, size):
#     open_set = minpq()
#     # closed_set = {}
#     open_set[str(start)] = 0
#     cost_so _far = {}
#     came_from = {}
#     cost_so_far[str(start)] = 0
#     came_from[str(start)] = None
#
#     for node, gn in open_set.popitems():
#         # closed_set.add(node)
#
#         if node == str(goal):
#             print("FIN !")
#             return
#         for state in _neighbors(size, np.fromstring(node, dtype=int)):
#             if state in closed_list:
#                 continue
#             fn = (gn + 1) + manhattan(np.fromstring(node, dtype=int), goal, size)
#             if fn

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
    # start = Node(start)

    # Our two sets, it's easier to use sets than lists because of the hash, it
    # is only O(1) to find if a state is allready
    # open_list = set()
    # closed_list = set()

    open_list = set()
    closed_list = set()
    # Initialize the open list
    open_list.add(str(start))
    # open_list[start.key()] = start

    came_from = {}
    g_score = {}
    f_score = {}

    came_from[str(start)] = None
    g_score[str(start)] = 0
    f_score[str(start)] = manhattan(start, goal, size)

    heap = PriorityQueue()
    # heap.put(start.cost, start)
    heap.put(0, start.tolist())

    # Variables asked by the subject:
    stats = {'time_complexity': 1,  # Total number of states ever selected in open list
             'size_complexity': 0,  # Maximum number of states represented at the same time in lists
             'moves': 0}            # Number of moves required to transition from first state to goal state

    while open_list:
        current = np.asarray(heap.get())

        if np.array_equal(current, goal):
            _retracePath(came_from, current, stats, size)
            return

        # del open_list[current.key()]

        closed_list.add(str(current))
        # closed_list[current.key()] = current

        open_list.remove(str(current))
        # print(open_list)
        # open_list.pop(current.key())

        for state in _neighbors(size, current):

            # if (state.key() in closed_list and state.cost >= closed_list[state.key()].cost) or (state.key() in open_list and state.cost >= open_list[state.key()].cost):
                # continue
            # else:

            # if state.key() in closed_list:
            #     continue
            # if state.key() in open_list:
            #     if state.cost < current.cost:
            #         current.cost = state.cost
            #         current.parent = state.parent

            # if state.key() not in open_list or state.cost < open_list[state.key()].cost:

            # else:
            # if state.key() not in closed_list or state.cost < closed_list[state.key()].cost:

            if str(state) in closed_list:
                continue
            state_g_score = g_score[str(current)] + 1 # Pour BONUS modifier ce + 1 en 0 ou autre pour breadth ou greedy
            if str(state) not in open_list or state_g_score < g_score[str(state)]:
                open_list.add(str(start))
            # if state_g_score >= g_score[str(state)]:
                # continue
                came_from[str(state)] = current
                g_score[str(state)] = state_g_score
                f_score[str(state)] = state_g_score + manhattan(start, goal, size)
                # heuristic = manhattan(current.state, goal, size)
                # print("heuristic: {}, cost: {}".format(heuristic, state.cost))
                # fn = state.cost + heuristic
                # if state.cost >=
                # open_list.add(state)
                # open_list[state.key()] = state

                heap.put(f_score[str(state)], state.tolist())
                open_list.add(str(state))
                stats['time_complexity'] += 1
                stats['size_complexity'] = max(stats['size_complexity'], len(open_list))
                # print("open_list: ", open_list)

    return
