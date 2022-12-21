# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab5_5

def zodiac_element(year):# year % 12 ,the remainder of each division are zodiac
    if(year % 12 == 4):#ปีหนูเริ่มที่ค.ศ 4 อิงตามโจทย์ที่ให้ปีหนูมา และเรียงสัตว์ตามปีไปเรื่อยๆเลย
        zodiac = ("Rat")
    elif(year % 12 == 5):
        zodiac = ("Ox")
    elif(year % 12 == 6):
        zodiac = ("Tiger")
    elif(year % 12 == 7):
        zodiac = ("Rabbit")
    elif(year % 12 == 8):
        zodiac = ("Dragon")
    elif(year % 12 == 9):
        zodiac = ("Snake")
    elif(year % 12 == 10):
        zodiac = ("Horse")
    elif(year % 12 == 11):
        zodiac = ("Goat")
    elif(year % 12 == 0):
        zodiac = ("Monkey")
    elif(year % 12 == 1):
        zodiac = ("Rooster")
    elif(year % 12 == 2):
        zodiac = ("Dog")
    elif(year % 12 == 3):
        zodiac = ("Pig")
    #find the element #ธาตุทั้ง5วนครบ10พอดี ไม่ต้องคิดอะไร เซตแต่ละธาตุไว้ตามเลขเลย
    if(year % 10 == 0 or year % 10 == 1 ):#remainder 0,1 is Metal
        element = 'Metal'
        return ("%s %s"%(element,zodiac))
    elif(year % 10 == 2 or year % 10 == 3):#remainder 2,3 is Water
        element = 'Water'
        return ("%s %s"%(element,zodiac))
    elif(year % 10 == 4 or year % 10 == 5):#remainder 4,5 is Wood
        element = 'Wood'
        return ("%s %s"%(element,zodiac))
    elif(year % 10 == 6 or year % 10 == 7):#remainder 6,7 is Fire
        element = 'Fire'
        return ("%s %s"%(element,zodiac))
    elif(year % 10 == 8 or year % 10 == 9):#remainder 8,9 is Earth
        element = 'Earth'
        return ("%s %s"%(element,zodiac))
#Wood        Fire        Earth      Metal    Water ##check with % 10
#1984-1985 1986-1987 1988-1989 1990-1991 1992-1993 

# **Conclusion** 
#0and1 Metal 
# 2and3 Water 
# 4and5 Wood 
# 6and7 Fire 
# 8and9 Earth


def main():
    years =  int(input())
    print(zodiac_element(years))

if __name__ == "__main__":
    main()