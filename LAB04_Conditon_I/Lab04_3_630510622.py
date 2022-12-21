# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab4_3

#Concept this assignment is find the maximum of exp
#exp = 1 : 12 ; (pidgey : candy)
#1 pidgey 12 candy = 1 Pidgeotto and 500exp
#pidgey or Pidgeotto can change to 1 candy
#p = pidgey
#c = candy
#use exp = 1 : 12 first time and use 1 : 11 because change pidgeotto to candy 
def calculate_p2p_evolve_exp(p, c):
    if(p <= 0):#no pidgey = 0 exp
        exp = 0
        return(exp)   
    elif(c / p == 12):#if c is divisible by b,there is no pidgey left
        c = 0
        exp = p*500
        c = c + p
        return(exp)
    elif(c / p == 11):# 33 / 3 exp = (500*p)-500  because not enough candy
        a = c // 11#all divide by 11 
        exp  = a*500 
        return (exp-500)#exp - 500 because solved the problem with a 1 : 11
    else:#(c / p != 12)
        if(p >= c):#pidgey >= candy
            a = c//11# all divide
            p = p-a # how much the pidgey will decrease
            c = c - (11*a)#The number of candies left after removing that it cannot be converted to Pidgetto
            exp = 500 * a
#In conclusion, in the first round, take c // 11 so that the number of turns can be converted to Pidgetto            
            x = c - 13 # candy not enought find number to change pidgey to candy
            x = abs(x)
            p = p -   x # change pidgey to candy
            b = p // 12 # in the end Pidgetto(candy) = 1
            b = b + 1 
            exp = exp + (500*b)#exp round1 + exp round2; round2 is candy not enought
            return (exp)
        else: # p < c 2 case are pidgey enought and not enought
            a = c//11 #all devide
            if((p-a) <= 0):#pidgey not enought
                z = a - p #all devide - all pidgey
                exp = (a - z)*500 #find the number pidgey is 0 and *500 to change to maximum exp
                return (exp)
            else:#pidgey < candy ;in the end candy not enought
                exp = 500*a #round 1               
                p = p-a                         
                c = c - (11*a) #Remnants after dividing
                x = c-13 # how much c will enought for p
                x = abs(x) 
                p = p - x # change pidgey to candy
                b = p // 12 # in the end Pidgetto(candy) = 1
                b = b + 1 
                exp = exp + (500*b) #exp round1 + exp round2; round2 is candy not enought
                return (exp)

def main():
    pidgey = int(input())
    candy = int(input())
    print(calculate_p2p_evolve_exp(pidgey,candy))

if __name__ == "__main__":
    main()    


#แบบใช้loop
"""def calculate_p2p_evolve_exp(p,c):
    # p = นก
    # c = ลูกอม
    # ถ้านก บวก ลูกอม 12 ลูก = 500 exp
    exp = 0
    while p > 0:
        if(p > 0 and c < 12):
            c = abs(c)
            need = 12 - c
            c += need
            p -= need
            if(p <= 0):
                break
        if(p > 0  and c >= 12):
            exp += 500
            c += 1
        p -= 1
        c -= 12
    print (exp)
def main():
    p = int(input())
    c = int(input())
    calculate_p2p_evolve_exp(p,c)
if __name__ == "__main__":
    main()"""
