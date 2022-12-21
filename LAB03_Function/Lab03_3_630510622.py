# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab3_3

from math import sqrt
def octagon_area(x):
    squre = x*x#all of area
    triangle = (0.5*(x/3)*(x/3))*4
    area = squre - triangle
    return area
#---- find octagon in squre --> squre - triangle = area    
def main():
    x = int(input())
    area = octagon_area(x)#area when cut squre and triangle
    print (area)#area octagon
if __name__ == "__main__":
    main()  