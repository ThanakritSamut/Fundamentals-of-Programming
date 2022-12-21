#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab9_5

def reverse_num(num):
    if(num == 0):
        return 0
    else:
        return((num%10)*(10**(len(str(num))-1))) + reverse_num(num//10)

def main():
    num = int(input())
    print(reverse_num(num))

if __name__ == "__main__":
    main()