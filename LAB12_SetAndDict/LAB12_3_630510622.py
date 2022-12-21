#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab12_3

import math
def prime_factor(n):#find prime factor for co-prime of 2 number
    prime_factors = []
    while n % 2 == 0:#case number is even number 
        prime_factors.append(2)
        n = n / 2
    i = 3#start with 3
    while i <= math.sqrt(n):
        while n % i == 0:
            prime_factors.append(int(i))
            n = n / i
        i += 2
    if n > 2:#if n is prime factor more than 2
        prime_factors.append(int(n))
    return prime_factors
def coprime_factor(a,b):#find coprime
    list_a1 = prime_factor(a)#get a to prime factor ex. 180 -> 2 x 2 x 3 x 3 x 5
    #print(list_a1)
    list_b1 = prime_factor(b)#get b to prime factor ex. 74 -> 2 x 37
    #print(list_b1)
    list_result = []
    for i in list_a1:#check coprime with number prime factor
        if(i in list_b1):#number must be same with to list
            add_loop = min(list_b1.count(i),list_a1.count(i))#check how many coprime of i (i is prime factor)
            for j in range(add_loop):#add i to list_result
                list_result.append(i)
            list_a1 = list(filter(lambda a:a != i,list_a1))#get i out of list
            #because for i in list_a1 and list_a2 
            list_b1 = list(filter(lambda a:a != i,list_b1))#get i out of list
        add_loop = 0
        if(list_a1 == [] or list_b1 == []):#if add all coprime and no prime factor in list break the loop
            break
    list_result = sorted(list_result)#sorted co-prime
    return(list_result)

def main():
    a = int(input())
    b = int(input())
    print(coprime_factor(a,b))
if __name__ == "__main__":
    main()