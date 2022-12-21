def kth_digit(number,k):
    number = abs(number)
    k = abs(k)
    return (number // 10**k) % 10
# 1234 // 10**3 % 10
def main():
    number = int(input())
    k = int(input())
    position_of_k = kth_digit(number,k)
    print (position_of_k)
if __name__ == "__main__":
    main()    