#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab10_2

#จงเรียงลำดับoutput ของ list_a(ชนิด int) list_b(ชนิด float) และ list_c(ชนิด string) ตามลำดับ 
# หากไม่มีชนิดใด ให้return empty list --> [] 
#Hint คำสั่ง isinstance ไว้สำหรับเช็คว่าตัวแปรนั้นตรงกับชนิดที่กำหนดมั้ย
#คัดกรองชนิดข้อมูลในlist_x ก่อน เพราะ ตอนแรกที่รับเข้ามาเป็น string ทั้งหมด
import string
def classify(list_x):
    list_a = []# int
    list_b = []# float
    list_c = []# string
    for i in list_x:#ไล่เช็คในlist_x แต่ละตัวด้วย i
        if(isinstance(i,int)):#ถ้า i เป็น int เข้า if นี้
            list_a.append(i)#เพิ่ม i เข้าไปในlistของint (list_a)
        elif(isinstance(i,float)):#ถ้า i เป็น float เข้า if นี้
            list_b.append(i)#เพิ่ม i เข้าไปในlistของfloat (list_b)
        else:#isinstance(i,str) #ถ้า i เป็น string เข้า else
            list_c.append(i)#เพิ่ม i เข้าไปในlistของstring (list_c)
    return (list_a,list_b,list_c)# return list int,float,string ตามลำดับ

def main():
    list_x = []#สร้างempty list เพื่อเก็บค่าที่input ไว้ใน list
    while True:
        list_x1 = input()# input ค่าไปเรื่อยๆจากloop while เพราะเราไม่รู้ว่าข้อมูลที่เข้ามาเป็นอะไรบ้าง
        if list_x1 == "":#หากinputเป็นwhite space ให้ ออกจากwhile ถือว่าการรับinput สิ้นสุด
            break
        list_x.append(list_x1)#เก็บค่าที่inputไว้ในlist_xที่สร้างไว้ในบรรทัดที่ 24
    j = 0#สำหรับแยกคิดกรณีทศนิยมกับจำนวนเต็ม สร้างเพื่อไม่ให้เปลี่ยนค่า i
    for i in list_x:#for สำหรับคัดกรองข้อมูลในlist #ไล่จำนวนสมาชิกโดยตัวแปร ร
        if i[0] in string.digits:#ถ้าตัวอักษรตำแหน่งที่0เป็นตัวเลข-->(string.digits)
            i = float(i)#เปลี่ยน i ตัวนั้นเป็นfloatก่อน 
            if(i % 1 == 0):#หลังจากเปลี่ยนเป็นfloat ถ้าหาร1แล้วเท่ากับ0 ถือว่า i ตัวนั้นเป็น int
                i = int(i)#แปลงเป็น int
                list_x[j] = i#เก็บไว้ในตำแหน่งที่ j ## j จะเปลี่ยนค่าไปพร้อม i จากบรรทัดที่ 40
            else:#ถ้าหาร i ไม่เท่ากับ 0 จะเข้า else (ตัว i ที่อ่านได้เป็นทศนิยม)
                i = float(i)
                list_x[j] = i#ถ้าเป็นfloat (เข้าelse) เก็บไว้ในตำแหน่งเดียวกับ i 
        j += 1#เพิ่ม j ตาม i ## j คือ index i คือลำดับในlist

    print(classify(list_x))

if __name__ == "__main__":
    main()