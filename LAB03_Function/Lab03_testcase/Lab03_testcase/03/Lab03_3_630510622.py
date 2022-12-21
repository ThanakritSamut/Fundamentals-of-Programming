from math import sqrt
def octagon_area(x):
    area = 2*(x*x)*(1+sqrt(2))
    return area
def squre(x):
    squre = (x*3)**2
    return squre

def main():
    x = int(input())
    area = octagon_area(x)
    area2 = squre(x)
    print (area2 - area)
if __name__ == "__main__":
    main()    
