def kth_digit(number,k):
    #x = ((x//1000)*1000) + ((x//100%10)*100) + ((x//10%10)*10) + (x)    
    number = (number // 10**k) % 10
    return number

def set_kth_digit(number,k,value):
    minus = (number // 10**k)%10
    answer = (number - minus*(10**k)) + value*(10**k)
    return answer
    



def main():
    number = int(input())
    k = int(input())
    value = int(input())
    answer = set_kth_digit(number,k,value)
    print (answer)
main()    
#1234
#2
#1
#1234 - 200 + 1*100
#1124    
#1000 + 200 +30 +4
#x*10^3 + x*10^2 + x*10 + x
# %number