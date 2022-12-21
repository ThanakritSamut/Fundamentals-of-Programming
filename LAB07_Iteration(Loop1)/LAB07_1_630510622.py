# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab7_1

def sum_prime_in_range(x,y): # function sum prime number x to y
    divide = 2 # 'divide' check can divided or not
    checker = False#checker to check 'divide' prime or not
    result = 0
    count = 0
    for i in range (x,y+1):#x = start , y = stop
        checker = False # reset check when new i 
        divide = 2 # resit divide when new i
        while(divide < i):
            if(i % divide == 0):#divided ; first i = 3
                checker = True #divide = not prime
                i += 1
                break#if that divide is not prime break and change to next divide number
            else:# x % divide != 0
                divide += 1#change to next divide number
        if(checker == False):#if divide = i and checker is False (i is not prime)
            result += i#plus the prime number
            count += 1
    print(count)
    return result
#เริ่มต้นเช็คว่าxเป็นจำนวนเฉพาะมั้ยโดยการเพิ่มตัวหารจนถึงsqrt(x) ถ้าหาร!=0เลยให้บวกค่าxนั้นไปเก็บในresult
#เมื่อxเปลี่ยน ให้set divide เป็น 2เหมือนเดิมและค่อยๆเพิ่มdivideเช็คเลขนั้นๆว่าหารลงตัวมั้ยถ้าไม่ลงตัวเลยให้เอามาใส่ในresult

def main():
    x = int(input())
    y = int(input())
    print(sum_prime_in_range(x,y))

if __name__ == "__main__":
    main()