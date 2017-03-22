import cython

cdef int manhattan(int x_1, int y_1, int x_2, int y_2):
	return abs(x_1 - x_2) + abs(y_1 - y_2)
