import argparse
import sys
import os
from timeit import default_timer as timer
from goal_generator import goal_generator
from a_star import solve
from parsing import parse
from puzzle_generator import puzzle_generator
from isSolvable import isSolvable
import time

# TODO: Implement IDA*


def _argparser():
    """Parse arguments using argparse library, returns a dictionnary with
    values."""

    def _file(parser, x):
        if not os.path.exists(x):
            parser.error("The file {} does not exist".format(x))
        else:
            return x

    def _size(parser, x):
        x = int(x)
        if x < 3:
            parser.error("Wrong size. Should be > 2.")
        else:
            return x

    parser = argparse.ArgumentParser(description='This software solve n-puzzle using A-star algorithm')
    parser.add_argument('filename', nargs='?', type=lambda x: _file(parser, x), default=None, help='text file describing the n-puzzle initial state')
    parser.add_argument('--heuristic', type=str, default='manhattan distance', choices=['manhattan distance', 'nSwap', 'euclidian distance', 'out row column','breadth'], help="choose the heuristic function used by the algorithm. Default to manhattan_distance.")
    parser.add_argument('--size', type=lambda x: _size(parser, x), default=3, help='choose a particular size to random generated n-puzzle. Default set to 3.')
    parser.add_argument('--viz', type=bool, default=False, help='')
    parser.add_argument('--greedy', type=bool, default=False, help='activate the greedy best first search (g(x) = 0))')
    args = vars(parser.parse_args())
    return args


def main():
    # Parse arguments
    args = _argparser()

    # Check and parse
    if args['filename'] is not None:
        npuzzle, size = parse(args['filename'])
        goal = goal_generator(size, dim=1)
        if not isSolvable(npuzzle, goal, size):
            sys.exit("Puzzle is not solvable")
    else:
        size = args['size']
        goal = goal_generator(size, dim=1)
        npuzzle = puzzle_generator(size, goal)

    print("--- Start:", npuzzle)
    print("--- Solving puzzle using A-star and {}".format(args['heuristic']))
    start = time.time()
    solve(npuzzle, goal, args)
    print("Solved in {:0.3f} seconds".format(time.time() - start))
    # astar(npuzzle, goal, args['size'])

    print("--- END")

if __name__ == '__main__':
    main()