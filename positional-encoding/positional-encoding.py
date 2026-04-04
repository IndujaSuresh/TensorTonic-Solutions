import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    # pass
    positions = np.arange(seq_len).reshape(seq_len,1)

    num_freqs = int(np.ceil(d_model / 2))

    frequencies = 1.0 / (base ** (np.arange(0, d_model, 2) / d_model)).reshape(1, num_freqs)
    A = np.empty([seq_len, d_model])
    sin_v = np.sin(positions*frequencies)
    cos_v =  np.cos(positions*frequencies)
    if (d_model%2 == 0 ):
        A [:, 0::2] = sin_v
        A [: , 1::2] = cos_v
    else:
       A[:,0::2] = sin_v[:,:num_freqs]
       A[:,1::2] = cos_v[:,:d_model//2]

    return A
   