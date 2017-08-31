import cython


cdef from_1d_to_2d(int size, int coord_1d):
    """Convert 1D coordinates into 2D coordinates from 0 to size - for a square.

    Args:
        size (int): square's size.
        coord_1d (int): 1 dimension coordinate.

    Returns:
        i, j (int, int): 2D coordinates with i (equivalent to x) and j (y).
    """
    i = int(coord_1d / size)
    j = int(coord_1d % size)
    return i, j


cdef from_2d_to_1d(size, i, j):
    """Convert 2D coordinates into 1D coordinates from 0 to (size - 1) - for a
    square.

    Args:
        size (int): square's size.
        i(int): x equivalent.
        j(int): y equivalent.

    Returns:
        coord_1d (int): 1D coordinates.
    """
    return i * size + j
