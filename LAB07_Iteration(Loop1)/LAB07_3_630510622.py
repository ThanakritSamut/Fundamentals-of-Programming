# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab7_3

#All you need to have in this problem are head and base of triangle you can print head and base without loop
#point '.' have 2 increments 1 3 5 7 9...n+2

def triangle(n):
    print("*")#top of triangle have head '*'
    for i in range (n-2):
        print("*",end="")#first * when next floor 
        for j in range(((i+2)*2)-3):
            print(".",end="")# point between *
        print("*")# * closed triangle
    for i in range(n):#base
        print("*",end=" ")#print base of triangle '* ' n times
    print("")#next line
def main():
    n = 7
    triangle(n)
if __name__ == "__main__":
    main()