def get_div(c, z_0=0, thresh=4, max_steps=25):
    z=z_0
    for i in range(max_steps):
        if (z*z.conjugate()).real>=thresh:
            return 0
        z=z*z +c
    return 1

def get_iter(c, z_0=0, thresh=4, max_steps=25):
    z=z_0
    for i in range(max_steps):
        if (z*z.conjugate()).real>=thresh:
            return i
        z=z*z +c
    return max_steps
