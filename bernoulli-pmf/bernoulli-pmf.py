import numpy as np
def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    e =[]
    # Write code here
    for i in x:
        if i == 0:
            c = 1-p
        else:
            c = p
        e.append(c)
    mean = p
    variance = p * (1-p)
    # print("c",e)
    return tuple((np.array(e) , float(mean), float(variance)))

