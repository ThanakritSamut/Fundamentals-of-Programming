def reverse_digits(x):
    x = ((x%10)*1000) + ((x//10%10)*100) + ((x//100%10)*10) + (x//1000%10)
    return x
    

def main(): 
    x = int(input())
    x = reverse_digits(x)
    print ("%04d"%x)
main()

#1234 --> 4321