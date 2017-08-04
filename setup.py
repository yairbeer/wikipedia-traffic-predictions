from distutils.core import setup
from Cython.Build import cythonize

setup(name='smape function', ext_modules=cythonize("smape.pyx"),)
