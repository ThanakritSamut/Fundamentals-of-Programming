  # 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab3_5
#เปลี่ยนnumberหลักที่kเป็นvalue
def kth_digit(number,k):   
    number = (number // 10**k) % 10
    return number #function lab03_4
#--Swith Position--
def set_kth_digit(number,k,value):#1234,2,5
    minus = (number // 10**k)%10#result first position #minus = (1234 // 100)%10 = 12 % 10 = 2 #หาตำแหน่งที่ต้องการเปลี่ยน
    answer = (number - minus*(10**k)) + value*(10**k)#process to switch digits ex. 1234 - 2*(10**2) + 5*(10**2) = (1234 - 200) + 500 = 1534 
    return answer
#--function main--
def main():
    number = int(input())
    k = int(input())
    value = int(input())
    answer = set_kth_digit(number,k,value)#Position switched
    print (answer)
if __name__ == "__main__":
    main()    
