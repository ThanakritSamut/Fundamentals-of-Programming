#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab10_5

#แปลงเลขเป็นคำอ่านภาษาอังกฤษ

def three_digits_to_word(n):
    unit_list=["","one","two","three","four","five","six","seven","eight","nine","ten"
    ,"eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty"
    ,"fifty","sixty","seventy","eighty","ninety"]
    n = int(n)
    lens = len(str(n))
    number = n
    unit_hundred = ""
    if(lens == 3):#กรณี เลขหลักร้อย
        hundred = n//100
        lens -= 1
        number = number - (hundred*(10**2))
        unit_hundred += unit_list[hundred] + " hundred"
    if(lens == 2 and number >= 10 ):#กรณีเลขหลักสิบ
        if(number < 20 and number >= 10):
            if(n // 100 == 0):
                unit_hundred += unit_list[number]
            else:
                unit_hundred += " " + unit_list[number]
            lens -= 2 
        else:#number >= 20
            number = number // 10 # 2
            if(n // 100 == 0):
                unit_hundred += unit_list[(number*10)-(9*(number-2))]
            else:
                unit_hundred += " " + unit_list[(number*10)-(9*(number-2))]
            lens -=1
            if(n%10 != 0):
                unit_hundred += "-"
    if(lens == 1 or number < 10):#กรณีเลขหลักหน่วย
        if(number >= 10 or lens == 2):
            unit_hundred += " " +unit_list[int(str(n)[-1])]#number % 10
        else:
            unit_hundred += unit_list[int(str(n)[-1])]
    return unit_hundred

def num_to_word(num):
    if (num == 0):
        return "zero"
    num = str(1000000000000 + num)
    num = num[1:]
    list_a = []
    #sub_list = []
    j = 0
    string = ""
    for i in num:
        string += i
        j += 1
        if(j % 3 == 0 and j != 0 ):
            list_a.append(string)
            string = ""
    result = list(map(three_digits_to_word,list_a))
    answer = ""
    if(result[0] != ""):
        seperate = " billion "
        answer += result[0] + seperate
    if(result[1] != ""):
        seperate = " million "
        answer += result[1] + seperate 
    if(result[2] != ""):
        seperate = " thousand "
        answer += result[2] + seperate
    if(result[3] != ""):
        answer += result[3]
    return answer 

        


def main():
    n = int(input())
    #print(three_digits_to_word(n))
    print(num_to_word(n))

if __name__ == "__main__":
    main()