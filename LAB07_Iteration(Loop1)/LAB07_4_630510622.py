# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab7_4

def life_path(n):
    number = 0
    answer = 0
    new_answer = 0
    while(n != 0):#ทำจนกว่า n จะเป็น 0 # บวกหลักทั้งหมด
        number = n % 10 # find digit number
        n = n // 10#ten digits to digit
        answer += number#plus ten digits and digit
        k = answer#k is answer
    if(answer < 10):#if plus less than 10 return answer
        return answer
#plus all of number and process again
    else:#หลักทั้งหมดบวกกัน > 10
        while(k >= 10):#if k >= 10 plus until one digit
            while(answer != 0):# like loop in line 10 to 14
                number = answer % 10# reset ค่า number ใหม่ เอา answer % 10 เก็บไว้ในnumber
                answer = answer // 10
                new_answer += number
            k = new_answer
            answer = k
            new_answer = 0#reset new_answer when answer >= 10 (loop again)
        return k

def main():
    n = int(input())
    print (life_path(n))

if __name__ == "__main__":
    main()