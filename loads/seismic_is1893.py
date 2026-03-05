import math

def base_shear(W, Z, I, R, Sa_g):

    Ah = (Z/2) * (I/R) * Sa_g

    Vb = Ah * W

    return Vb
