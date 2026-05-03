import numpy as np
import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    # pass
    if rng is None:
        rng = np.random.default_rng()  

    x = np.array(x)
    n = len(x)

    boot_means = [] 

    for i in range(n_bootstrap):
        indices = rng.integers(0, n, size=n)
        sample = x[indices]
        boot_mean = np.mean(sample)
        # print("boot_mean",boot_mean)
        boot_means.append(boot_mean)

    alpha = 1 - ci
    lower = np.quantile(boot_means, alpha / 2)
    upper = np.quantile(boot_means, 1 - alpha / 2)

    # print("boot_means",boot_means)
    boot_means = np.array(boot_means)
    return boot_means, lower, upper
