# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab5_3
from datetime import date#call datetime,datetime will check leap year 

def count_down_to_songkran(d,m,y):
    years = y
    month = m
    days = d
    today = date(years, month, days)
    if(today.month <= 4 and today.day <= 13):#Not yet due (days 13 month 4) #ถ้าอยู่ในเดือน4
        songkran = date(years, 4, 13)
        delta = today - songkran
        delta = abs(delta)
        #print("today.month <= 4 and today.day <= 13")
        return(delta.days)
    elif(today.month <= 3 and today.day > 13):# Not yet due. Just in case month <= 3 and days > 13
        songkran = date(years, 4, 13)
        delta = today - songkran
        delta = abs(delta)
        #print("today.month <= 4 and today.day > 13")
        return(delta.days)      
    else:#today > 13 and month > 4
        songkran = date(years+1, 4, 13)
        delta = songkran - today
        delta = abs(delta) 
        #print("today > 13 and month > 4")
        return(delta.days)

def main():
    days = int(input())
    month = int(input())
    years = int(input())
    print(count_down_to_songkran(days,month,years))
if __name__ == "__main__":
    main()