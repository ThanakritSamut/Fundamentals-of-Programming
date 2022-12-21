# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab4_4

# round up or down 
# round up remaining more than or equl 5
# round down remaining less than 5
def round_to_int(x):
    if(x <= 0):# x <= 0
        x = abs(x)#abs because modulus in line 13
        a = x * 10#decimal cannot modulus
        if(a % 10 >= 5):
            x = x + 1#round up
            x = int(x)
            return (x*-1)#change to negative number 
        elif(a % 10 < 5):
            x = int(x)#round down
            return (x*-1)#change to negative number           
    elif(x > 0):
        a = x * 10  # x * 10 because function if cannot  % decimal  ;2.6 = 26      
        if(a % 10 >= 5):#modulus because need to know round up or down if modulus >= 5 round up ; 26%10 = 6
            x = x + 1#round up 
            x = int(x)
            return(x)
        elif(a % 10 < 5):#modulus because need to know round up or down if modulus < 5 round down 
            x = int(x)#round down 
            return (x)   
def main():
    x = float(input())
    print (round_to_int(x))
if __name__ == "__main__":
    main()            
