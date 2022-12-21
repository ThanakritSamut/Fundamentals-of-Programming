# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab8_5

def decode(code_table,text):#change number to charater[i]
    for line in text.split('\n'):#แยกบรรทัดที่inputเข้ามาเพื่อprintตามบรรทัด # separate line to set
        for i in line.split():#แยกตัวอักษรเป็นลำดับ (str) # separate char #เจอช่องว่างให้แยก #ทำจนบรรทัดนี้เสร็จ
            i = int(i)#แปลงstr เป็น int # str to int
            if(i >= len(code_table) or i < 0):#หากตัวเลขนั้น > index ให้แสดงค่า underscore หรือ ค่า < 0 if i out of range print underscore '_'
                print("_",end="")
            else:#i in range print code_table[index] --> index is number counting
                print(code_table[i],end="")#แสดงอักขระ[i] # print the char
        print("")#ขึ้นบรรทัดใหม่ # next line
# เก็บอักขระในindexแต่ละช่องของตัวแปร
def main():
    code_table = 'aceiklmr-'
    text ='''-1
5 3 4 2
3 1 2 8 1 7 2 0 86'''
    decode(code_table,text)
if __name__ == "__main__":
    main()
