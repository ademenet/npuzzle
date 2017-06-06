from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy

setup(name="goal_generator", include_dirs=[numpy.get_include()], ext_modules=cythonize("goal_generator.pyx"))
setup(name="heuristic", ext_modules=cythonize("goal_generator.pyx"))
setup(name="parsing", include_dirs=[numpy.get_include()], ext_modules=cythonize("parsing.pyx"))
setup(name="is_solvable", include_dirs=[numpy.get_include()], ext_modules=cythonize("isSolvable.pyx"))
