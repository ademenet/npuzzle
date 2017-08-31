import argparse
import sys
import os
import time
from goal_generator import goal_generator
from a_star import solve
from parsing import parse
from puzzle_generator import puzzle_generator
from isSolvable import isSolvable


def _argparser():
    """Parse arguments using argparse library, return a dictionnary with
    values."""

    def _file(parser, file_name):
        """Return file_name if file exists, display error and quit otherwise."""
        if not os.path.exists(file_name):
            parser.error("The file {} does not exist".format(file_name))
        else:
            return file_name

    def _size(parser, size):
        """Return size if > 2, display error and quit otherwise."""
        size = int(size)
        if size < 3:
            parser.error("Wrong size. Should be > 2.")
        else:
            return size

    parser = argparse.ArgumentParser(description='This software solve n-puzzle using A-star algorithm')
    parser.add_argument('filename', nargs='?', type=lambda x: _file(parser, x), default=None, help='text file describing the n-puzzle initial state')
    parser.add_argument('--heuristic', type=str, default='manhattan distance', choices=['manhattan distance', 'nSwap', 'euclidian distance', 'out row column','breadth'], help="choose the heuristic function used by the algorithm. Default to manhattan_distance.")
    parser.add_argument('--algo', type=str, default="A-star",choices=['A-star','ida-star'], help='Choose the algorithm to solve the puzzle. Default : A-star')
    parser.add_argument('--size', type=lambda x: _size(parser, x), default=3, help='choose a particular size to random generated n-puzzle. Default set to 3.')
    parser.add_argument('--viz', default=False, action='store_true', help='activate a visualisation with moving tile')
    parser.add_argument('--greedy', default=False, action='store_true', help='activate the greedy best first search (g(x) = 0))')
    parser.add_argument('--time', default=False, action='store_true', help='display the duration')    
    args = vars(parser.parse_args())
    return args


def main():
    """Main function to be called."""
    # Parse arguments
    args = _argparser()

    # Check and parse
    if args['filename'] is not None:
        npuzzle, args['size'] = parse(args['filename'])
        goal = goal_generator(args['size'], dim=1)
        if not isSolvable(npuzzle, goal, args['size']):
            sys.exit("Puzzle is not solvable")
    else:
        size = args['size']
        goal = goal_generator(size, dim=1)
        npuzzle = puzzle_generator(size, goal)

    print("--- Start:", npuzzle)
    print("--- Solving puzzle using {} and {}".format(args['algo'],args['heuristic']))
    start = time.time()
    solve(npuzzle, goal, args)
    if args['time']:
        print("Solved in {:0.3f} seconds".format(time.time() - start))

    print("--- END")

if __name__ == '__main__':
    main()
