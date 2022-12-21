# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab6_3

def factorize(x):
    divide = 2#set divide 2 because use to check can divided or not ** 1 can divided all of numbers.
    checker = False
    print("%d is"%x,end = "")#prime or not this message be output
    if(x == 2):# 2 is an exception; have this if because divide is 2 , 2 can check it odd or even
        print(" prime")
        return 0#return because not to be none
    while (x != 1):#divide until x is 1
        if(x % divide == 0):#if x divide evenly #divide หารลงตัว
            x = x / divide # divide to find next factor
            if(x != 1):#x after divide != 1
                print(" %d "%divide,end = "*")#divide is factor of x
            else:# x == 1 # when x = x / divide == 1,divide is last factor of x
                print(" %d"%divide)
            checker = True # have checker because check x is prime or not,if x can divide x isn't prime 
        else:# x % divide != 0
            divide = divide + 1 # plus divide to check x / divide until divide near sqrt(x) **line 23 
            if(divide > (x**0.5)):#define: The smallest prime factor of any integer will not exceed the square root of that number.
                if(checker == True):#print last factor without ' ' 
                    print(" %d"%int(x))#ปริ้นค่าx ก็คือตัวประกอบสุดท้าย
                break # เบรคตัวท้าย
    if(checker == False):# x can not divide by divide checker not change, checker is check that number prime or not
        print(" prime") 
def main():
    x = int(input())
    factorize(x)

if __name__ == "__main__":
    main()