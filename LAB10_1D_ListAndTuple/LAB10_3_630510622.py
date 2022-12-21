#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab10_3
# Rotate ตัวเลขในlistไปทางขวา ถ้า n เป็นบวก และหมุนตัวเลขในlistไปทางซ้าย ถ้า n เป็นลบ โดย **listเดิมที่ถูกrotateไม่เปลี่ยนค่า**
def nondest_rotate_list(list_a,n):
    lens = len(list_a)#นับจำนวนในlistเพื่อนำไปวนตัวเลขตามจำนวนในlist
    rotate = abs(n) % lens # จำนวนท่ี่วน
    list_b = []#สร้างlistว่าง เพื่อเก็บค่าตัวเลขใหม่ที่ถูกrotateแล้ว
    if n >= 0:#rotate ไปทางขวา
        first_index = rotate*-1#ตำแหน่งที่ถูกหมุนขวาตำแหน่งแรกคือตำแหน่งขวาสุดหรือก็คือ index[-1](ตำแหน่งสุดท้ายจะเริ่มหมุน)
        for i in range (lens):#เริ่มrotate lens ครั้ง
            list_b.append(list_a[first_index])#นำเลขไปใส่เรียงกันในlistจากซ้ายไปขวา
            first_index += 1#เพิ่มfirst_index เพื่อเพิ่มเลขในindexต่อไป
        return(list_b)#วนจนครบ ให้return list_b --> list ที่ถูก rotate เรียบร้อย
    else: # n < 0 rotate ไปทางซ้าย
        first_index = abs(rotate)#เริ่มหมุนที่ตำแหน่ง rotate
        for i in range (lens):# หมุนตามจำนวนข้อมูลในlist_a
            list_b.append(list_a[first_index])#นำเลขไปใส่เรียงกันในlistจากซ้ายไปขวา
            first_index += 1#เพิ่มindexเพื่ออ่านข้อมูลในlist_aตัวถัดไป
            if first_index == lens:#ถ้าfirst_index == lens แล้วหมายถึงตำแหน่งวนไปถึงขวาสุดของlist_aแล้ว เหลือซ้ายสุดให้เริ่มที่ตำแหน่งซ้ายสุดคือ 0
                first_index = 0#ตำแหน่งซ้ายสุด
        return(list_b)#วนครบ return list_b
def main():
    list_a = []
    while True:
        try:#inputจนกว่าผู้ทดสอบจะinput white space
            list_a1 = int(input())
            list_a.append(list_a1)
        except(ValueError):#หากเจอError ValueError ให้ break loop while
            break
    n = int(input())#เลื่อน(ขวา,ซ้าย)กี่ตำแหน่ง
    print(nondest_rotate_list(list_a,n))
if __name__ == "__main__":
    main()
