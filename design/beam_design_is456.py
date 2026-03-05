import math

def beam_flexural_design(Mu,b,d,fck,fy):

    Mu_lim = 0.138*fck*b*d**2

    if Mu < Mu_lim:

        Ast = (0.5*fck/fy)*(1-math.sqrt(1-4.6*Mu/(fck*b*d**2)))*b*d

    else:
        raise Exception("Doubly Reinforced Beam Required")

    return Ast
