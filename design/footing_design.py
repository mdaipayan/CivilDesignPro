import math

def footing_size(Pu, SBC):

    area = Pu / SBC

    side = math.sqrt(area)

    return side
