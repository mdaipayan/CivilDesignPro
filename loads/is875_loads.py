def dead_load_slab(thickness, density=25):
    return thickness * density

def floor_finish_load():
    return 1.0

def live_load(residential=True):
    if residential:
        return 2.0
    else:
        return 3.0
