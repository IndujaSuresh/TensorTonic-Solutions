import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    B= [[0]*len(A) for _ in range(len(A[0]))]
    # print(B)
    # print(len(A))
    # print(len(A[0]))
    for i in range(len(A)):
        for j in  range(len(A[0])):
        #    B[i][j] = A[i][j]
            B[j][i] = A[i][j]
    return(np.matrix(B))
