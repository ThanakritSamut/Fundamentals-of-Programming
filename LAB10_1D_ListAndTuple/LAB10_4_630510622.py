#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab10_4

#rotate ตัวเลขไปทางซ้าย n เป็นลบ ไปทางขวา n เป็นบวก โดยไม่สร้างlistใหม่ (เปลี่ยนแปลงlist เดิม)

def dest_rotate_list(list_a,n):
    lens = len(list_a)#นับจำนวนครั้งที่จะวนลูปเพื่อ rotate
    rotate = abs(n) % len(list_a)#ตำแหน่งที่เริ่มหมุน
    if n >= 0:#หมุนขวา
        first_index = rotate*-1#ตัวเริ่มหมุน
        for i in range(lens):
            if first_index >= 0:
                list_a.append(list_a[first_index])#เพิ่มข้อมูลในlistตำแหน่งfirst_index
            else:
                list_a.append(list_a[first_index-i])#เพิ่มข้อมูลในlist first_index-i เพราะ เมื่อappend ข้อมูลแล้ว 
                #ให้วนขวาจนถึงตำแหน่งที่ -1 list_a หากวนไปถึงขวาสุดของlist_aเดิมให้เริ่มวนจากซ้ายของlist_aเดิม
            first_index += 1#เพิ่มindexไปเรื่อยๆ เข้า if เมื่อนับตำแหน่งจากขวามาซ้ายจนครบตำแหน่งที่0 
        del(list_a[0:lens])#ลบlist_aเดิมทั้งหมดแล้วเหลือlist_aที่appendไปในโปรแกรม
    else:#n < 0
        first_index = abs(rotate)#ตำแหน่งที่เริ่มตามตำแหน่งเลยเพราะเริ่มหมุนซ้าย(ตำแหน่งซ้ายหลังตำแหน่งที่เลือกต้องอยู่ขวา)
        for i in range (lens):# วนลูปตามจำนวนข้อมูลในlist_aตอนแรก
            list_a.append(list_a[first_index])
            first_index += 1
            if first_index == lens:#append ไปจนกว่าตำแหน่งจะเท่ากับจำนวนในlist_a(ขยับซ้ายไปlens-first_indexครั้ง)แล้ว
                #เริ่มนับจากซ้ายมาขวาจนครบloop
                first_index = 0
        del(list_a[0:lens])#ให้list_aเหลือเฉพาะตำแหน่งที่สลับแล้ว

def main():
    list_a = []
    while True:
        try:
            list_a1 = int(input())
            list_a.append(list_a1)
        except(ValueError):
            break
    n = int(input())
    print(dest_rotate_list(list_a,n))

if __name__ == "__main__":
    main()