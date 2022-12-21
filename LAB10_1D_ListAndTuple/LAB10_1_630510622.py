#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab10_1

#ข้อนี้เช็คว่าตัวอักษรภาษาอังกฤษใน str1 และ str2 เหมือนกันหรือไม่ ไม่นับ เว้นววรค ตัวเลข อักขระพิเศษ ตัวอักษรใหญ่-เล็ก = ตัวเดียวกัน
import string # จำเป็นต้องใช้ฟังก์ชัน string
def is_anagram(str1,str2):
    result1 = "" #ประกาศตัวแปรเพื่อเปรียบเทียบตัวอักษรกับstr2 
    result2 = "" #ประกาศตัวแปรเพื่อเปรียบเทียบตัวอักษรกับstr1
    str1 = "".join(sorted(list(str1.lower())))#ทำการเรียงตัวอักษรและปรับให้เป็นตัวพิมพ์เล็ก 
    #str.lower ปรับ string ทั้งหมดเป็น lower
    #list เอาแต่ละตัวใส่ในlist
    #sorted เรียงลำดับแต่ละตัวในlist
    #"".join แปลงแต่ละตัวให้้เป็นstring --> (จาก "" ด้านหน้า)
    str2 = "".join(sorted(list(str2.lower())))#ทำการเรียงตัวอักษรและปรับให้เป็นตัวพิมพ์เล็ก
    #ปรับเป็นตัวพิมพ์เล็กทั้งสองเพื่อเปรียบเทียบให้เป็นชนิดเดียวกัน
    for ch in str1:#for เช็คstr ใน str1
        if(ch in string.ascii_letters):#คัดกรองตัวอักษรภาษาอังกฤษเท่านั้น(ascii_letters)
            result1 += ch#ถ้าch ไล่ไปเจออักษรภาษาอังกฤษให้เก็บไว้ในตัวแปร result1
    for ch in str2:#for เช็ค str ใน str2
        if(ch in string.ascii_letters):#ถ้า ch ไล่ไปเจออักษรภาษาอังกฤษให้เก็บไว้ในตัวแปร result2
            result2 += ch#คัดกรองตัวอักษรภาษาอังกฤษเท่านั้น(ascii_letter)
    if (result1 == result2):#ถ้าตัวอักษรในresult1 == result2 (เช่น abc == abc)--> เข้า if นี้ return True
        return True
    else:#ถ้า result1 != result2 (ตัวอักษรไม่เหมือนกัน) return False
        return False

def main():
    str1 = input("")
    str2 = input("")
    print(is_anagram(str1,str2))

if __name__ == "__main__":
    main()