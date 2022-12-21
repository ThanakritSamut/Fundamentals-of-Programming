# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab3_1
#หาปริมาตรทรงกลม
import math
def find_r_from_surface_area(surface_area): #ชื่อฟังก์ชัน
    pi = math.pi # pi ในข้อนี้ใช้ math.pi เพื่อให้ค่าตรงกับโจทย์
    r = ((surface_area/4/pi)**0.5)#สูตรทรงกลม = 4 pi r^2 // ย้ายข้างให้เหลือแค่ r 
    return r
def sphere_volume(radius): # set radius = r ตรงฟังก์ชัน main
    pi = math.pi # ใช้ pi = math.pi
    volume = ((4/3)*pi*(radius**3)) # สูตรหาปริมาตร(volume) พื้นที่ทรงกลม 
    return volume
def main():
    surface_area = float(input("input surface area: "))
    radius = find_r_from_surface_area(surface_area) #รัศมี = คำนวณในฟังก์ชัน
    volume = sphere_volume(radius)
    print("volume = {0:.2f}".format(volume))
main()
