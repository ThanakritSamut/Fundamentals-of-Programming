# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab8_4

#check big and small who is more than ?

import string # import to use function
def uniform(line):
    BIG = string.ascii_uppercase # set BIG is large letter
    SMALL = string.ascii_lowercase # set SMALL is small letter
    big_letter = 0 # set value
    small_letter = 0 # set value
    for i in line: # count line #line คืออักขระที่รับเข้ามา #บรรทัดนี้ไล่อักขระทีละตัวแล้วเช็คว่าตัวใหญ่หรือเล็ก
        if i in BIG:# check character line is big or not and count
            big_letter += 1
        elif i in SMALL:# check character line is small or not and count
            small_letter += 1
    if(small_letter > big_letter):#if small_letter is more than big_letter return all of line is small
        return (line.lower())
    elif(small_letter < big_letter):#if big_letter is more than small_letter return all of line is big
        return (line.upper())
    else:#small_letter == big_letter // print the line in first type letter
        if line[0] in BIG:
            return(line.upper())
        else:
            return(line.lower())


def main():
    line = input()
    print(uniform(line))
if __name__ == "__main__":
    main()