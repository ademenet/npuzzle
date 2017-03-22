from distutils.core import setup
from Cython.Build import cythonize

setup(name="goal_generator", ext_modules=cythonize("goal_generator.pyx"))
