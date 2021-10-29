# Binary step activation function. Returns 1 for n>=0. Otherwise return -1.

import numpy as np

def binaryStep(dataIn):
    # conditional on data-type
    if isinstance(dataIn, (int, float, np.int64)):
        return 1 if dataIn >= 0 else -1
    elif isinstance(dataIn, np.ndarray):
        return np.array([binaryStep(xi.item()) for xi in dataIn])
