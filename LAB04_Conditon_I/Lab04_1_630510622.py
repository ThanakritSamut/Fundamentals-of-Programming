# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab4_1

def love6(first, second):#function "love6"
    if (first == 6 ):#input(1) = 6
        return(True)
    elif (second == 6):#input(2) = 6
        return(True)
    elif (first + second == 6):#input(1) + input(2) = 6
        return(True)
    elif abs(first - second ) == 6:#input(1) - input(2) = 6
        return(True)        
    else:
        return(False)    
def main():
    first = int(input())
    second = int(input())
    print (love6(first,second))
if __name__ == "__main__":
    main()