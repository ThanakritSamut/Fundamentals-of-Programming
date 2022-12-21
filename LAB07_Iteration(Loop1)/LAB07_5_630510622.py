# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab7_5

#loop to count the digits
#pos is move n times
#num is number from keyboard
def rotate(num,pos):
    number = num
    count = 0
    while number > 0:#loop to count the digits
        number = number//10
        count = count + 1
    if(pos >= 0):#Move digits number left
        pos = pos % count#if pos = count number will same place,pos times is same place pos - count = times to moving #เลื่อนกี่ตำแหน่ง
        change1 = num % (10**pos)#find the number to move
        change2 = num // (10**pos)#change the number not moving
        return (change1*(10**(count-pos))+change2)#processing moving number 
    elif(pos < 0):#Move digits number right
        pos = abs(pos)#Change to abs because think only moving number
        pos = pos % count#if pos = count number will same place if not pos % count ex. pos = 7 will moving 7 times , 5 times is same place 7 - 5 = 2 times
        change1 = num // (10**(count - pos))#12345 --> 123 find number to move
        change2 = num % (10**(count - pos))#12345 --> 45change the number not moving
        return ((change2*(10**(pos))+change1))#processing moving number

def main():
    num = 481723
    pos = -7
    print(rotate(num,pos))
if __name__ == "__main__":
    main()

