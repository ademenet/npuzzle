# n-puzzle

This program solve n-puzzle game using A* algorithm. It's a _work in progress_.

## How to use this software?

```
make
python3 main.py ...
```

## Tips on Cython

With `Cython`, use:

```
cython file.pyx -a
```

To generate `.html` file with Cython's annotation telling you where your program is taking time.

## A* algorithm

A* helps us to find the shortest way to solve the n-puzzle. Here is a description of how it works.

In order to find the path, you need an first state and the goal state. The goal state is generated with `goal_generator`. It generates the n-puzzle with spiral solution (it is not the usual way). For example, for a 4 by 4 puzzle the goal will be:

```
 1  2  3  4
12 13 14  5
11  0 15  6
10  9  8  7
```

Once, we did this we need to check if inputs are valid. Indeed, some puzzles are unsolvable. We can check using the technique [described in this paper](http://cseweb.ucsd.edu/~ccalabro/essays/15_puzzle.pdf).

The solver is based on A* algorithm. To do so you need to create two lists: one for open 'states' and another for the 'closed' states. As we are going to explore the possibilities, we are going to maintain those lists to keep track of the previous and unexplored solutions. `neighbors` is the list of moves admissible to solve the puzzle.

```
def solve(current, end):
	neighbors = [-3, -1, 1, 3]
	open_set = []
	close_set = []
	open_list = [] # ???
```

We initiate `open_set` and `open_list` with the first state `start`.

```
	heapq.heappush(open_set, current)
	heapq.heappush(open_list, current)
```

Since we have states in our `open_set` or we didn't reach the goal state, we loop.

```
	while open_set:
		current = heapq.heappop(open_list) # take the current state (heapop gives us directly the one with the lowest heuristic - keep this in mind for later)
		if current == end:
			return retracePath(current) # retracePath() is just a function that go all the way up to recover the full solution and returns it in reverse order (from the first state to the goal state)
```

We actualize both lists. From `open_set` to `close_set`.

```
		open_set.remove(current)
		close_set.append(current)
```

Now we are going to generate the new states from our `current` state.

... to be done

Finally, we check if the new state is not in the close_set, otherwise that would mean we are going wrong way or we have already visited this state. If not, we compute the heuristic (in this example, it's manhattan) and we save the state, the heuristic, the parent and push it to the heap queue. As our heap queue is sorted, the next `current` initialization will be with the lowest heuristic.

```
			if tile not in close_set:
				tile.heuristic = abs(x_1 - x_2) + abs(y_1 - y_2)
				if tile not in open_set:
					open_set.add(tile)
					heapq.heappush(open_list, (tile.H, tile))
				tile.parent = current
```

## Some useful link that we used

- [Why can't we put python lists into a set?](http://stackoverflow.com/questions/1306631/python-add-list-to-set)
