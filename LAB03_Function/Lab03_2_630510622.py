# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab3_2

#-----reverse number using % ex. input(1234) ---> (4000+300+20+1) = 4321---- 
def reverse_digits(x):
    x = ((x%10)*1000) + ((x//10%10)*100) + ((x//100%10)*10) + (x//1000%10)
    return x   
    
#input x to using in function reverse and output x when finish in function
def main(): 
    x = int(input())
    x = reverse_digits(x)
    print ("%04d"%x)
if __name__ == "__main__":
    main()

"""def reverse_digits(x):
    number = x
    k = 3
    answer = 0
    for i in range(4):
        result = (number // (10**i) % 10)*(10**k)
        answer = answer + result
        k -= 1
    print (answer)

# x // (10**i % 10)*10**k

def main():
    x = 5421
    reverse_digits(x)
if __name__ == "__main__":
    main()"""
