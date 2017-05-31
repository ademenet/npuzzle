import numpy as np
import sys

def parse(filename, verbose=False):
    """Parse file text into 1D numpy array.
    
    Handle multiple type of errors:
        - blank lines
        - wrong comments (line do not begin with '#')
        - wrong size expected
        - expected size too small (size < 3)
        - no expected size before description

    Args:
        filename (str): file text path to open and parse.
        
    Returns:
        npuzzle (1D numpy array): n-puzzle, we don't know yet if it is solvable
	    or not.
    """
    size = 0
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "" or line.strip().isalpha():
                sys.exit("Wrong file format")
            if not line.startswith("#"):
                np_array = np.fromstring(line, dtype=int, sep=' ')
                if np_array.shape[0] == 1 and size == 0:
                    size = np_array[0]
                    npuzzle = np.array([], dtype=int)
                    if size < 3 : sys.exit("Expected size is too small")
                    if verbose : print("Expected size: ", size)
                elif np_array.shape[0] != 1 and size == 0:
                    sys.exit("No expected size, wrong format")
                elif size != 0 and np_array.shape[0] == size:
                    npuzzle = np.concatenate((npuzzle, np_array))
                else:
                    sys.exit("Wrong size")
    if npuzzle.shape[0] == size * size:
        limit = size * size - 1
        for nb in npuzzle:
            if nb > limit:
                sys.exit("Wrong format")
        if np.sum(np.arange(0, limit)) != np.sum(npuzzle):
            sys.exit("Wrong format")
        return npuzzle
    else:
        sys.exit("Wrong size")
