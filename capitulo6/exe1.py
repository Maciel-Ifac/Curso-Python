import numpy as np 

def polar_to_comp(r,phi):
    return r*(np.exp(*phi))

print(polar_to_comp(10,10))

