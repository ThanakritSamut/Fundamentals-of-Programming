 # 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab4_5

def nearest_odd(x):
    if(x >= 0):
        x = int(x)
        if(x % 2 == 0):
            x = x + 1
            return (x)
        else:
            return (x)       
    #========จำนวนเต็มลบ=======#
    else:#(x < 0)#-8854.2308 ##ปัดก่อนแล้วค่อยคำนวณ
        x = abs(x)#ขั้นแรกควรแปลงเป็นabsก่อนเพราะจะได้เข้าifได้ทุกกรณี
        if(x % 2 == 0):#if นี้สำหรับเลขลบที่หารลงตัวอยู่แล้วไม่มีทศนิยม(เลขคู่ที่ไม่มีทศนิยม)
            x = int(x)
            x = x - 1#เลขคี่ที่ติดลบมากที่สุดคือ จำนวนลบเข้าใกล้0 x - 1 เพราะแปลงเป็นabsในบรรทัดที่16
            return (x*-1)#แปลงกลับมาเป็นจำนวนลบ
        x = int(x)#ถ้าไม่เข้าifยังไงก็ต้องแปลงให้รู้ว่าเป็นคู่หรือคี่ผ่านคำสั่งint
        if(x % 2 == 0):#if นี้กรณีเลขลบคู่มีทศนิยมจะทำการปัดลงเพราะมีทศนิยม//จะต้องคืนค่าเลขคี่ที่ใกล้xที่สุด -2.1 กับ -2 เลขคี่ใกล้-2.1คือ-3 เลขคี่ใกล้-2คือเลข-1
            #ถ้าติดไม่มีทศนิยมจะเข้าifแรกก่อน ถ้าเข้าifนี้แสดงว่ามีทศนิยม ซึ่งจะเข้าifนี้ได้ต้องแปลงเป็นint(เป็นเลขคู่ที่มีทศนิยม)
            x = x + 1
            return (x*-1)
        elif(x % 2 != 0):#หารไม่ลงตัว #เป็นเลขคี่ ก็ตอบเลขคี่ตัวนั้น
            return(x*-1)            
#ติดกรณีจำนวนเต็มกับทศนิยมว่าจะปัดทิ้งหรือไม่ปัดทิ้ง
def main():
    x = float(input())
    print(nearest_odd(x))
if __name__ == "__main__":
    main()            
#จำนวนเต็มต้องได้น้อยลง เช่น -36 ต้องได้ -35
#-36.5ต้องได้ -37