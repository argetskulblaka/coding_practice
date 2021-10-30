# Positive linear (Rectified Linear) activation function.
# Return 0 for negative input. Otherwise linear.

import numpy as np

def posLin(dataIn):
    if isinstance(dataIn, (int, float, np.int64)):
        return 0 if dataIn < 0 else dataIn
    elif isinstance(dataIn, np.ndarray):
        return np.array([posLin(xi.item()) for xi in dataIn])
