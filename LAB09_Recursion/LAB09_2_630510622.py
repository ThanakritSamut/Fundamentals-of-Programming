#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab9_2

def n_to_10(n,num,i):
    if (num == 0):
        return 0
    else:
        result = (n**i) * (num%10)
        num = num // 10
        return (result + n_to_10(n,num,i + 1))
def n_base_to_10(n,num):
    return (n_to_10(n,num,i = 0))

def main():
    n = int(input())
    num = int(input())
    print(n_base_to_10(n,num))

if __name__ == "__main__":
    main()