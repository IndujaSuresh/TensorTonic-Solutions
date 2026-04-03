import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    c = np.dot(a,b)
    d = np.linalg.norm(a)
    e = np.linalg.norm(b)
    if ((d==0) or (e==0)):
        return 0
    else:
        return (c/(d*e))
    # pass