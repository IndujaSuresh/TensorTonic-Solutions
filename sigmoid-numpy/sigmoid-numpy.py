import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x, dtype=float)
    # Write code here
    if np.isscalar(x):
        sigmoid_x = 1 / (1 + np.exp(-x))
        print("sigmoid_x",sigmoid_x)
        return sigmoid_x
    else:
        sigmoid_x = (1/(1+np.exp(-x)))
        print("sigmoid_x",sigmoid_x)
        return sigmoid_x