# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab6_2

#float to binary เลขติดทศนิยมเป็นเลขฐาน2

def float_to_bin(x):
    if(x < 0):# float < 0
        x = abs(x)#change to positive number 
        k = x % 1#after decimal
        x = x // 1#before decimal
        result = 0#set value
        i = 0#set value
        j = -1#set value
        while x > 0:#find before decimal
            r = x % 2
            result = result + (r*(10**i))
            x = x // 2
            i = i + 1
        #result > 10**-1
        while (k % 1 != 0):# times 2 and check if that >= 1 or < 1
            k = k * 2
            if(k >= 1):
                r = 1
                result = result + (r*(10**j))#use result lastest value
            elif(k < 1):
                r = 0
                result = result + (r*(10**j))#use result lastest value
            j = j - 1#minus digits
            k = k % 1#set digits
        return (-1*result)#return negative number because x < 0
    else:#x >= 0#like x < 0 but not return negative number
        k = x % 1#เอาทศนิยม
        x = x // 1#เอาหน้าทศนิยม
        result = 0
        i = 0
        j = -1
        while x > 0:
            r = x % 2
            result = result + (r*(10**i))
            x = x // 2
            i = i + 1#เปลี่ยนหลัก +1 เพราะ i เริ่มต้นที่หลักแรก และการแปลงเป็นbinaryวิธีธรรมดาจะไล่เลขจากล่างไปบน บรรทัดนี้คือเรียงจากหลักหลังไปหลักหน้า
        #result = dec --> binary
        while (k % 1 != 0):#ทำจนกว่าค่าทศนิยจะเป็น0
            k = k * 2
            if(k >= 1):
                r = 1
                result = result + (r*(10**j))
            elif(k < 1):
                r = 0
                result = result + (r*(10**j))
            j = j - 1#เปลี่ยนหลัก
            k = k % 1 # เอาแค่ทศนิยม
        result = float(result)
    return (result)
def main():
    x = float(input())
    print(float_to_bin(x))
if __name__ == "__main__":
    main()