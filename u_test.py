import numpy as np
from goal_generator import goal_generator

# Goal generator testing
np.testing.assert_array_equal(goal_generator(3, 1), np.array([1, 2, 3, 8, 0, 4, 7, 6, 5]))
np.testing.assert_array_equal(goal_generator(4, 1), np.array([1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7]))

# Is solvable testing
