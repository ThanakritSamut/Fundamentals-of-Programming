#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab9_4

def series(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        if(n % 2 == 0): # even number
            return (2*series(n-1)+1)
        else:# n % 2 != 0 ## odd number
            return (2*series(n-1)-1)
def main():
    n = int(input())
    print(series(n))

if __name__ == "__main__":
    main()
# 0 1 3 5 11