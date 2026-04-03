import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    # pass
    a = np.sqrt(np.sum((np.array(x)-np.array(y))**2))

    # a = np.sqrt(np.sum(x-y)**2)
    return a
    