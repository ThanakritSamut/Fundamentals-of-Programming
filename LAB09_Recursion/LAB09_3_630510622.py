#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab9_3

import math
def is_prime_prime(n,divide):
    if(math.sqrt(n) < divide and n != 1):
        return True
    if(n % divide == 0 or n == 1):
        return False
    else:
        return(is_prime_prime(n,divide+1))

def is_prime(n):
    return(is_prime_prime(n,divide = 2))

def main():
    n = int(input())
    print(is_prime(n))

if __name__ == "__main__":
    main()