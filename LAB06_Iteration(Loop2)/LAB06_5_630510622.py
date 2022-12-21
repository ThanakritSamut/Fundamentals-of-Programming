# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab6_5
#เลขติดกันมากที่สุดกี่ตัว?
def longest_digit_run(n):
    k = n # k for check the digits of number
    r = 0 # r = digits of number
    count = 1 # counter
    save_count = 0 # max_count
    while k > 0:# check digit of number , r = round of for loop
        k = k // 10
        r = r + 1
    for i in range (r):#loops 'r' times
        num1= n % 10 # one digit
        n = n // 10 # change ten digit to one digit 
        num2 = n % 10 # num2 = one digit
        #do num1 and num2 because use the compare 2 of number to find the same number
        if(num1 == num2):#if one digit = ten digit
            count += 1
            if(count >= save_count):#save max digit in value save_count
                save_count = count
        else:#num1 != num2
            if(count >= save_count):#not change save_count # เซฟค่าsave_countเอาไว้มากที่สุด ถ้าcountมากกว่าsave_countเมื่อไหร่ค่อยเปลี่ยนค่า
                save_count = count
            count = 1#if num1 != num2 reset count because number is difference #รีเซตค่าcount แต่ save_countจะเก็บเอาไว้มากสุด
    return save_count
#สุดท้ายต้องn // 10 เพื่อตัดตำแหน่งที่คิดแล้วออก
#เช็คว่าเลขที่คำนวณเหมือนก่อนหน้ามั้ย ถ้าเหมือนให้ k = k + 1

def main():
    n = int(input())
    print(longest_digit_run(n))
if __name__ == "__main__":
    main()