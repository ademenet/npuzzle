import heapq
import numpy as np
from heuristic import getHeurstic
from utils import from_1d_to_2d, from_2d_to_1d
from termcolor import cprint


class PriorityQueue():
    """Not thread-safe PriorityQueue implementation."""
    def __init__(self):
        self.queue = []

    def display(self):
        """Display the queue. For debug purposes."""
        import copy
        heap = copy.copy(self.queue)
        while heap:
            print(heapq.heappop(heap))

    def put(self, priority, item):
        """Add one item to the queue, sorted according to priority."""
        heapq.heappush(self.queue, (priority, item))

    def get(self):
        """Return the first item in le queue."""
        return heapq.heappop(self.queue)[1]

    def length(self):
        """"Return the length of the queue."""
        return len(self.queue)


def display(state, size):
    """Display the state with 0 in red and others in white."""
    for i in range(size):
        for j in range(size):
            if state[i * size + j] == 0:
                cprint(state[i * size + j], 'red', end=' ')
            else:
                cprint(state[i * size + j], 'white', end=' ')
        print()
    print()


def _retracePath(came_from, current, stats, size):
    """Retrace the paths of all the states from initial to goal and display some
    more informations."""
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
        current (list): current state node.

    Return:
        list_neighbor (list of list): returns a copy of the possible neighbor,
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
            neighbor = tuple(copy)
            list_neighbor.append(neighbor)

    return tuple(list_neighbor)


def solve(start, goal, args):
    """Solve the puzzle using A* algorithm.

    Args:
        start (1D numpy array): starting state.
        goal (1D numpy array): goal state.
        args (dict): program args.

    Returns:
        display the solution.
    """
    # Initializing the dictionnaries. Dictionnaries in Python use hashmap, thus
    # accessing to keys is O(1).
    # We use a PriorityQueue - build on min heap queue, it is only O(n*log(n))
    # in worth case to be sort.
    came_from = {}
    g_score = {}            # Closed set
    heap = PriorityQueue()  # Open set
    size = args['size']
    heuristicFunction = getHeurstic(args['heuristic'])

    # We implemented two extra A-star types: breadth search and greedy search.
    # Breadth search is a particular A-star algorithm where heuristic is allways
    # equal to zero. Another name for it is Dijkstra (with all edge weighted to
    # 1, which is our case).
    # Greedy search is a particular A-star algorithm without distance/cost take
    # into account.
    g = 0 if args['greedy'] else 1

    goal = tuple(goal)
    start = tuple(start)
    came_from[str(start)] = None
    g_score[str(start)] = 0
    f_score = heuristicFunction(start, goal, size)
    bound =  f_score
    heap.put(0, start)

    algo = args['algo']

    stats = {'time_complexity': 1,  # Total number of states ever selected in open list
             'size_complexity': 0,  # Maximum number of states represented at the same time in lists
             'moves': 0}            # Number of moves required to transition from first state to goal state

    while heap:	
        if heap.length() > 0:
            current = heap.get()
            if current == goal:
                _retracePath(came_from, current, stats, size)
                return
        else:
            bound += 1
        for state in _neighbors(size, current):
            state_g_score = g_score[str(current)] + g
            if algo == 'ida-star' and state_g_score + heuristicFunction(state, goal, size) <= bound + state_g_score:
                if str(state) not in g_score or state_g_score < g_score[str(state)]:
                    came_from[str(state)] = current

                    g_score[str(state)] = state_g_score
                    f_score = state_g_score + heuristicFunction(state, goal, size)

                    heap.put(f_score, state)
                    stats['time_complexity'] += 1
                    stats['size_complexity'] = max(stats['size_complexity'], heap.length())
            elif algo == 'A-star':
                if str(state) not in g_score or state_g_score < g_score[str(state)]:
                    came_from[str(state)] = current

                    g_score[str(state)] = state_g_score
                    f_score = state_g_score + heuristicFunction(state, goal, size)

                    heap.put(f_score, state)
                    stats['time_complexity'] += 1
                    stats['size_complexity'] = max(stats['size_complexity'], heap.length())
            
    return
