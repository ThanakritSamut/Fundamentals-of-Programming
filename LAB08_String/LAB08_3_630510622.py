# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab8_3

def patterned_message(massage,pattern):#print massage in pattern
    massage = massage.replace(" ","")#set massage to close
    k = 0# set value
    for line in pattern.split('\n'):#นับบรรทัด # count line of pattern
        for i in line.split(","):#แจงแต่ละชุด #check the char
            for j in i:#ไล่ตัวอักษรไปเรื่อยๆจนเจอ*ค่อยใส่ตัวอักษรลงไป
                if(j != "*"):#if j != "*" print that char
                    print(j,end="")
                else:#j == "*" print massage[index]
                    print(massage[k],end="")
                    k += 1
                    if(k == len(massage)):#sort index ,if out of range reset index to zero.
                        k = 0
            print("")#ขึ้นบรรทัดใหม่ตอนจบแถว

def main():
    massage = "Three Diamonds!"
    pattern ='''     
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
    '''
    patterned_message(massage,pattern)
if __name__ == "__main__":
    main()