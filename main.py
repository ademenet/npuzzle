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

# TODO accelerer avec Cython et des optis python ! Cest soit lent : environ 1 min pour un 3 * 3, soit < 1 sec pour les plus facile, il faut etre a 10 sec

# BUG Parfois il ne sort pas par la sortie qui matche avec le final state, jai teste que sur des puzzles generes aleatoirement
# BUG Time and Size complexity sont pas bons, enfin, il faut verifier ce que cest exactement car il y a toujours 1 d'ecart/make


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
    stats = {
        'parsing': 0,
        'solving': 0,
    }
    
    if args['filename'] is not None:
        start = timer()
        npuzzle, size = parse(args['filename'])
        end = timer()
        stats['parsing'] = end - start
        goal = goal_generator(size, dim=1)
        if not isSolvable(npuzzle, goal, size):
            sys.exit("Puzzle is not solvable")
    else:
        if args['size'] > 2:
            size = args['size']
            goal = goal_generator(size, dim=1)
            npuzzle = puzzle_generator(size, goal)
        else:
            sys.exit("Size is too small")

    print("Initial state: ", npuzzle)

    print("--- Generating goal state")
    goal = goal_generator(size, dim=1)
    print("Goal state: ", goal)

    print("--- Solving puzzle using A-star")
    start = timer()
    solve(npuzzle, goal, args['size'])
    end = timer()
    stats['solving'] = end - start

    if args['stats']:
        print("Parsing took {} s. and solving {} s. for a total of {} s.".format(stats['parsing'],
                                                                              stats['solving'],
                                                                              stats['parsing'] + stats['solving']))
    print("--- END")

if __name__ == '__main__':
    main()
