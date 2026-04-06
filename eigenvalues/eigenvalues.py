import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    if not isinstance(matrix, list) or not matrix:
        return None

    if not isinstance(matrix[0], list):
        return None

    num_rows = len(matrix)
    
    try:
        if all(isinstance(row, list) and len(row) == num_rows for row in matrix):
            a = np.array(matrix)
            c = np.linalg.eigvals(a)
            return np.sort(c)
        else:
            return None
    except:
        return None
