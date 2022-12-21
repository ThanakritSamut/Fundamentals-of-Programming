import math
def find_r_from_surface_area(surface_area):
    pi = math.pi
    r = ((surface_area/4/pi)**0.5)
    return r
def sphere_volume(radius):
    pi = math.pi
    volume = ((4/3)*pi*(radius**3))
    return volume
def main():
    surface_area = float(input("input surface area: "))
    radius = find_r_from_surface_area(surface_area)
    volume = sphere_volume(radius)
    print("volume = {0:.2f}".format(volume))
main()    
