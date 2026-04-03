import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    # pass
    a = [[0]* len(v) for _ in range(len(v))]
    for i in range(len(v)):
        a[i][i] = v[i]
        
    return (np.matrix(a))
