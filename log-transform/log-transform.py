import math
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    s =[]
    # Write code here
    for i in values:
        r = math.log1p(i)
        s.append(r)
    return s