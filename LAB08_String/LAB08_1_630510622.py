# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab8_1

#print square n x n
#sep is letter cut between
def square_frame(n,sep=' '):#(3<=n<=25)
    x = len(sep)#นับตัวsepเพื่อใช้ในการปริ้นค่าในทุกแถว ยกเว้น แถว1และแถวสุดท้าย count sep for print the row except first row and second
    count = (n*2)+(x*(n-1))-4#นับตัวอักษรในชั้นแรกทั้งหมด -4 เนืองจากตัวแปรนี้ต้องใช้ในลูปที่คิดบริเวณส่วนกลางของสี่เหลี่ยม count คือ char ในส่วนกลาง
    #count all of char to use in middle square
    b = 0#ไว้สำหรับ วนตัวอักษร ถ้าหลุด range for loop index again when out of range
    lens = 0#ไว้สำหรับcheckว่าตัวอักษรเกินขอบเขตที่ควรอยู่หรือไม่ check char out of range or not
    for i in range(n):#ลูปนี้สำหรับแสดงผลตัวเลขแถวด้านบนสุด
        print("%02d"%(i+1),end="")#print Top square
        if(i < n-1):#ปริ้นตัวคั่นระหว่างเลข
            print("%s"%sep,end="")#print separator (sep) ปริ้นค่าระหว่างเลข
    print("")#เว้นวรรคเพื่อขึ้นลูปแสดงผลค่าตรงกลาง#new line to print middle square
    g = ((n*2)-2)*2#เลขตัวแรกแถว2#first number row 2 (left of squre)
    for i in range(n-2):#คิดแยกกรณีบนกับล่าง จึงเหลือที่ไม่ได้คิดอีก n-2 แถว # n is row of all n-2 is middle square
        print ("%02d"%g,end="")#ปริ้นเลขแถว2 print 'g' in line 19
        while lens < count: #ลูปนี้สำหรับปริ้นค่าsep loop for print sep// count is value of sep in middle squre
            print("%s"%sep[b],end="")#print loop sep 
            b = b + 1#เพิ่ม index # next index of sep
            if (b == x):#ถ้าหลุด index ให้วนกลับมา index แรก if out of range return to index[0]
                b = 0#set index[0]
            lens = lens + 1#ปริ้นsep1ตัวlensบวก1ตัว (เช็คขอบเขตส่วนกลางว่าเกินรึยัง) ถ้าเกินในบรรทัดนั้นก็จะออกloopในบรรทัดนั้น
            # check range of middle is out of range or not if out of range while loop will stop and next line
        lens = 0#จะขึ้นบรรทัดใหม่set ขอบเขตให้เป็น0 # reset range of sep
        print("%02d"%(n+(i+1)))#ตัวเลขแถว2ขวาสุดของสี่เหลี่ยม (ตัวปิดแถว)# i จะเพิ่มขึ้น ตัวเลขปิดแถวก็จะเพิ่มขึ้นทีละ1
        #print number right of square
        g = g - 1#ขึ้นแถวที่3,4,5,6... next right squre row
    k = ((n*2)-2)+n#k เป็นตัวแปรสำหรับใส่ในloopปิดท้ายกรอบสี่เหลี่ยม (แถวล่างสุด) #Botton row
    for i in range(n):#loop ปริ้น จำนวนเลข n ครั้ง
        print("%02d"%k,end="")#แสดงค่าเลขซ้ายล่างสุด # print left botton row
        k = k-1#ลดเลขลงมาเพื่อต่อไปแสดงค่าที่น้อยลงไปทางขวา # decrease number to sort to right
        if(i < n-1):#ปริ้นค่าsepต่อเลขที่ปริ้นออกมา print separator (sep) # n-1 เพราะ i เริ่มที่0 เช่น n-1 = 3 i จะวนแค่ 0 1 2
            print("%s"%sep,end="")#จบloopแรกขึ้นตัวถัดไปจากคำสั่ง end="" print sep and prepare to next number with end=""
    print("")#next line 
def main():
    n = int(input())
    sep = input()
    square_frame(n,sep)
if __name__ == "__main__":
    main()