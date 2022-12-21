#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab9_1

def gcd(x , y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
def main():
    x = int(input())
    y = int(input())
    print(gcd(x, y))
if __name__ == "__main__":
    main()