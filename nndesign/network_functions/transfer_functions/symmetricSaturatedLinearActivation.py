# Symmetric saturated linear activation function.
# returns -1 if < -1 
#          1 if > 1
# otherwise n

import numpy as np

def satLinS(dataIn):
    if isinstance(dataIn, (int, float, np.int64)):
        if (dataIn < -1):
            return -1
        elif (dataIn > 1):
            return 1
        else:
            return dataIn
    elif isinstance(dataIn, np.ndarray):
        return np.array([satLinS(xi.item()) for xi in dataIn])
