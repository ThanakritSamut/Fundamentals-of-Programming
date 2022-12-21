# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab6_1

#Find pow หาเลขยกกำลัง x = ฐาน y = เลขยกกำลัง
def int_power(x,y):
    result = 1#set result
    if(y == 0):#define exponent = 0, result = 1 
        result = 1
        return result
    else:#exponent != 0
        if(y > 0):#exponent > 0
            for i in range (y):#x*x  y times 
                result = result * x #รอบที่ 0 result = x
            return (result)
        elif(y < 0):#y = exponent define a^-n = 1/a^n
            y = abs(y) #abs y to for loop
            for i in range (y):#x*x  y times 
                result = result * x
            return (1/result)
def main():
    x = float(input())#x = base
    y = int(input())#y = exponent
    print(int_power(x,y))
if __name__ == "__main__":
    main()
#ถ้าหารแล้วเศษ != 0 ให้ round 3 ไป
#ถ้าฐานเป็นเลขทศนิยม ให้ round 3
#ไม่ใช่ ก็ลูปธรรมดา