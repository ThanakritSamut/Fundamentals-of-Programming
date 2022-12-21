# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab3_4

#---output digit(k) number---
def kth_digit(number,k):
    number = abs(number)# number >= 0 
    k = abs(k)#หลักของnumber ต้องเป็นค่าบวก
    return (number // 10**k) % 10  # % คือ เอาถึงหลักไหน
#---function main---    
def main():
    number = int(input())
    k = int(input())
    position_of_k = kth_digit(number,k) #
    print (position_of_k)#result 
if __name__ == "__main__":
    main()    