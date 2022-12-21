# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab7_2

def test_digit_count():
    pass


def digit_count(x,base=10):#function count digits of dec --> base
    count = 0
    x = abs(x)#negative number to positive number
    while(x > 0):
        x = x // base#count 'count' times when divided 
        count += 1
    return count

def main():
    x = int(input())
    base = int(input())
    print(digit_count(x,base))
if __name__ == "__main__":
    main()