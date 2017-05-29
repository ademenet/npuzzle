import pandas as pd

def parsing(filename):
    """This function parses a file into 1D array.

    Args:
        filename (str): filename path to open.

    Returns:
        npuzzle (1D numpy array): our npuzzle, but we don't know yet if it is
            solvable or not.
    """
    datas = pd.read_csv(filename, sep=' ', delim_whitespace=True, comment='#')
    fo = open(filename, "rw+")
    line = fo.readline()
    while line:
        print(line)
        if 
    fo.close()
