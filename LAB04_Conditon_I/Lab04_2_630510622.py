# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab4_2
#เรียงค่ามากสุด ค่ากลาง ค่าน้อยสุด
#First find max and min 
def my_max_mid_min(a, b, c):
    if (a>b):#if a > b ; max = a 
        MAX = a
        MIN = b
    else:#if a < b ; max = b
        MAX = b
        MIN = a
#Before comparing here,we have to find max and min for comparing c (line 8 to 13)        
#Then compare c with MAX and MIN       
    if (c > MAX):#if c > max then c is max
        MAX = c
    if (c < MIN):#if c < min the c is min
        MIN = c
    MID = (a + b + c) - (MAX + MIN)#find mid
# for exameple a = 23 b = 50 c = 3
# find max and min with (a,b); max = b min = a
# then compare with c ; c < min , min = c
# MID = (23 + 50 + 3) - (max + min)#max = b , min = c
#MIN = 76 - 53 = 23,a is 23 then mid = a
    print("max = %d"%MAX)
    print("mid = %d"%MID)
    print("min = %d"%MIN)    
                     
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    my_max_mid_min(a,b,c)
if __name__ == "__main__":
    main()
