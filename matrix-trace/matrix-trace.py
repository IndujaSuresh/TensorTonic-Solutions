import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    B =0 
    # Write code here
    if len(A) == len (A[0]):
        for i in range(len(A)):
            B+=A[i][i]
        return B
                 
