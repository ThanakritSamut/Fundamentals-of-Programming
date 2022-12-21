# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab5_1

def euclid_dis(x1,y1,x2,y2):#Find center distance of two circle x1,y1 and x2,y2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5#distance #หาระยะทางระหว่างจุด2จุด

def intersects(x1,y1,r1,x2,y2,r2,epsilon=10**-6):
    dis_circle = euclid_dis(x1,y1,x2,y2)#get return function to var
    result = 0
    if(abs(dis_circle-(r1+r2)) < epsilon ):#circle outside and touching #วงกลมติดกันด้านนอก เหมือน ระยะทางระหว่างจุดกับรัศมีเท่ากัน
        result = 0#
    elif (dis_circle + min(r1,r2) > max(r1,r2) and (dis_circle < (r1 + r2))):#circle inside and touching#วงกลมแตะกันด้านใน #ตัดกัน
        result = 1
    else: #(dis_circle > (r1 + r2)) #circle not touching no intersect #วงกลมไม่ตัดไม่แตะ ระยะทาง มากกว่า รัศมีทั้งสองบวกกัน
        result = -1
    return result

def main():
    x1 = float(input())
    y1 = float(input())
    r1 = float(input())
    x2 = float(input())
    y2 = float(input())
    r2 = float(input())
    print(intersects(x1,y1,r1,x2,y2,r2))
if __name__ == "__main__":
    main()
    """print("dis_circle = ",dis_circle)
    print("r1 + r2 = ",r1+r2)
    print("r1 - r2 = ",(r1-r2))
    print("dis_circle - (r1+r2) = ",(dis_circle-(r1+r2)))
    print("dis_circle - (r1-r2) = ",((dis_circle)-(r1-r2)))"""