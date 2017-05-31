from goal_generator import goal_generator
from a_star import solve
import argparse
from parsing import parse
from puzzle_generator import puzzle_generator
import sys
from isSolvable import isSolvable

# TODO implementer le A*: allmost done

# TODO implementer 3 heuristiques qui ont du sens
# 	TODO manhattan
#	TODO one other
#	TODO one other

# TODO faire le retour du nombre de opened states
# TODO faire le retour du nombre de states en memoire durant la recherche (opened + closed)
# TODO faire le retour du nombre de moves qu'il a fallut
# TODO faire le retour des differents etats qui menent a la solution

# TODO faire un parser
# TODO faire un detecteur de solvalbilite

# TODO fournir differntes maps pour les tests de la correction

# TODO bonuses

import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This software solve n-puzzle using A-star algorithm')
    parser.add_argument('filename', nargs='?',
                        type=str, default=None,
                        help='text file describing the n-puzzle initial state')
    parser.add_argument('-h1', '--manhattan', action='store_true', help='choose manhattan heuristic')
    parser.add_argument('-h2', '--nswap', action='store_true', help='choose n-swap heuristic')
    parser.add_argument('-h3', '--euclidean', action='store_true', help='choose euclidean heuristic')
    parser.add_argument('-s', '--size', type=int, default=3, help='choose a particular size to random generated n-puzzle')
    args = vars(parser.parse_args())

    if args['filename'] is not None:
        npuzzle = parse(args['filename'])
        if not isSolvable(npuzzle):
            sys.exit("Puzzle is not solvable")
    else:
        if args['size'] > 2:
            npuzzle = puzzle_generator(args['size'] * args['size'])
        else:
            sys.exit("Size is too small")

    print("Start: ", npuzzle)

    print("--- Generating goal state")
    goal = goal_generator(args['size'], dim=1)
    print("Goal: ", goal)

    print("--- Solving puzzle using A-star")
    solve(npuzzle, goal, args['size'])

    print("--- END")
    # start = [1, 3, 2]
    # end = [1, 2, 3]
    # solve(neighbors, current, end)
    # start = [6, 5, 4, 1, 0, 8, 7, 2, 3]
    # start = [3,5,0,1,4,2,7,6,8]
    # start = [5,3,7,1,6,2,0,8,4]
    # start = [8,1,7,5,4,6,2,3,0]
    # goal = goal_generator(3, 1)
    # TODO: format goal
    # goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    # print("start: {} \ngoal: {}".format(start, goal))
    # parent = solve(start, goal, 3)

    # def main():
    # 	start = time.time()
    # 	result = goal_generator(3, 1)
    # 	end = time.time()
    # 	print(result)
    # 	print("total time exec: {}".format(end - start))

    # main()
