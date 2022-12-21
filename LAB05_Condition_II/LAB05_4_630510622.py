# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab5_4
#สี่เหลี่ยมสองอันซ้อนกันมั้ย? ดูตำแหน่งตามรูปในโจทย์
def is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2):
    #False is not overlapped 
    if(l2 > l1+w1):  #ถ้า xซ้ายB > xขวาA
        return False
    elif(l2+w2 < l1):  #ถ้า xขวาB < xซ้ายA
        return False
    elif(t2 > t1+h1):  #ถ้า yล่างB > yบนA
        return False
    elif(t2+h2 < t1):  #ถ้าyบนB < yล่างA
        return False
    #True is overlapped
    else:
        return True
def main():
    l1 = int(input())
    t1 = int(input())
    w1 = int(input())
    h1 = int(input())
    l2 = int(input())
    t2 = int(input())
    w2 = int(input())
    h2 = int(input())
    print(is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2))
    
if __name__ == "__main__":
    main()