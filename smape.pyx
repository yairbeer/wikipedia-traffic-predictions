from __future__ import division
import numpy as np

# "cimport" is used to import special compile-time information
# about the numpy module (this is stored in a file numpy.pxd which is
# currently part of the Cython distribution).
cimport numpy as np

# We now need to fix a datatype for our arrays. I've used the variable
# DTYPE for this, which is assigned to the usual NumPy runtime
# type info object.
DTYPE = np.int

# "ctypedef" assigns a corresponding compile-time type to DTYPE_t. For
# every type in the numpy module there's a corresponding compile-time
# type with a _t-suffix.
ctypedef np.int_t DTYPE_t


def smape(np.ndarray[DTYPE_t, ndim=2] y_true, np.ndarray[DTYPE_t, ndim=2] y_prediction):
	cdef int n_rows = y_true.shape[0]
	cdef int n_cols = y_true.shape[1]
	cdef int i
	cdef int j
	cdef np.ndarray smape_results = np.zeros([y_true.shape[0], y_true.shape[1]], dtype=DTYPE)

	for i in range(n_rows):
		for j in range(n_cols):
			denominator = (np.abs(y_true[i, j]) + np.abs(y_prediction[i, j])) / 200.0
			if denominator == 0:
				smape_results[i, j] = np.abs(y_true[i, j] - y_prediction[i, j]) / denominator
	return smape_results