# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab5_2

def is_p_triple(a,b,c):#check the 3 value are triple
    #Find the maximum to get in 'c' 
    if(a >= b):#หาmaxเพราะสูตรคือ max = รูท mid^2 + min^2 *การบวกกันสลับที่กันได้อยู่แล้วเพราะฉะนั้นหาแค่max
        max_ = a
        min_ = b
        mid_ = c
    elif(b >= a):
        max_ = b
        min_ = a
        mid_ = c
    if(c >= max_):#max_ = b; b = 4 #ถ้าcมากกว่าmaxที่หามา ก็ให้ตัวอื่นเป็นmid หรือ min ไปเลย เข้าหลักการคอมเม้นบรรทัดที่8
        max_ = c
        min_ = a
        mid_ = b
    if (max_ == ((min_**2) + (mid_**2))**0.5):#if 3 number are triple call True #เข้าสูตรเช็คไป
        return True
    else:#not triple False
        return False


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(is_p_triple(a,b,c))
if __name__ == "__main__":
    main()