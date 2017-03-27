from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(name="goal_generator", include_dirs=[numpy.get_include()], ext_modules=cythonize("goal_generator.pyx"))
setup(name="heuristic", ext_modules=cythonize("goal_generator.pyx"))
