# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab8_2

def is_palindrome(x,b):
    #หาเลขฐาน n วนไปจนกว่าจะหารไม่ได้ # find base n until can't devide
    #หาเลขฐานคือหารเอาเศษไปเรื่อยๆ # find base is %
    num = x # line 9 to 12 set value
    i = 0
    result = 0 # ประกาศตัวแปรresult //declare value
    count = 0# ประกาศตัวแปร count // declare value
    if(x < b):#if x < b result = 1 digit // is palindrome // b are 2 to 9 (base)
        return True
    while x > 0:
        r = x % b#เศษที่ได้ # remainder
        result = result + (r*(10**i))#เอาเศษที่ได้ไปไว้ตำแหน่งแรก # get remainder to result
        x = x//b#แปลงxสำหรับหาเศษใหม่ #next digits
        i = i + 1#เพิ่มiเพื่อเพิ่มหลัก #add i to change digit number
    #print(result)
    num = result # get num to result
    while num > 0:#count digit of num
        num = num // 10
        count += 1
    result = str(result)#change to string
    new = int(count/2)#find middle of number
    front = result[0:new]#check front of number
    back = result[-new:]#check back of number
    new_back = (back[::-1])#reverse back number to check is same front or not
    #print("front = %s"%front)
    #print("back = %s"%new_back)
    if(front == new_back):#if front == new_back is palindrome
        return True
    else:#front != back # not palindrome
        return False
    #ถ้ากลับเลขของbackแล้วได้ = front ตอบ True
#test input ฐาน 10 base ฐาน
#ถ้าตัวต่อไปหลังจากตัวที่!=0เป็น0จนจบให้เก็บไว้ counter+1

def main():
    x = 2657
    b = 3
    print (is_palindrome(x,b))
if __name__ == "__main__":
    main()
#2657 3
#6 7 