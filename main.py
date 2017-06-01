import argparse
import sys
from timeit import default_timer as timer
from goal_generator import goal_generator
from a_star import solve
from parsing import parse
from puzzle_generator import puzzle_generator
from isSolvable import isSolvable

# TODO faire le retour du nombre de opened states
# TODO faire le retour du nombre de states en memoire durant la recherche (opened + closed)
# TODO faire le retour du nombre de moves qu'il a fallut
# TODO faire le retour des differents etats qui menent a la solution

def _argparser():
    """Parse arguments using argparse library, returns a dictionnary with values."""
    parser = argparse.ArgumentParser(description='This software solve n-puzzle using A-star algorithm')
    parser.add_argument('filename', nargs='?',
                        type=str, default=None,
                        help='text file describing the n-puzzle initial state')
    parser.add_argument('-h1', '--manhattan', action='store_true', help='choose manhattan heuristic')
    parser.add_argument('-h2', '--nswap', action='store_true', help='choose n-swap heuristic')
    parser.add_argument('-h3', '--euclidean', action='store_true', help='choose euclidean heuristic')
    parser.add_argument('-s', '--size', type=int, default=3, help='choose a particular size to random generated n-puzzle')
    parser.add_argument('-st', '--stats', action='store_true', default=False, help='display the timer stats for the principal functions')
    args = vars(parser.parse_args())
    return args

def main():
    args = _argparser()

    if args['filename'] is not None:
        start = timer()
        npuzzle, size = parse(args['filename'])
        end = timer()
        if args['stats']: print("Parsing took: ", end - start, " s")
        if not isSolvable(npuzzle, size):
            sys.exit("Puzzle is not solvable")
    else:
        if args['size'] > 2:
            npuzzle = puzzle_generator(args['size'] * args['size'])
        else:
            sys.exit("Size is too small")

    print("Initial state: ", npuzzle)

    print("--- Generating goal state")
    goal = goal_generator(args['size'], dim=1)
    print("Goal state: ", goal)

    print("--- Solving puzzle using A-star")
    start = timer()
    solve(npuzzle, goal, args['size'])
    end = timer()
    if args['stats']: print("Solving took: ", end - start, " s")

    print("--- END")

if __name__ == '__main__':
    main()
