from math import pi

def volume_of_a_sphere(radius):
    return (4/3)*(pi*radius**3)

print('%.3f' % volume_of_a_sphere(11))