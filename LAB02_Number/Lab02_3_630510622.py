# 630510622
# ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab02_3

#y = mx+b 
print("First Equation")#Show the first equation
m1 = float(input("Input m1: "))#input m1 from the keyboard
b1 = float(input("Input b1: "))#input b1 from the keyboard
print("Second Equation")#Show the second equation
m2 = float(input("Input m2: "))#input m2 from the keyboard
b2 = float(input("Input b2: "))#input b2 from the keyboard
x = (b1-b2)/(m2-m1)#find x from the input value เอาสมการyทั้งสองตัวมาเท่ากับกัน แล้วย้ายข้างให้เหลือแค่ x 
y = (m1*x) + b1#find y from the input value แทน x ลงในสมการที่1
print ("The point of intersection is at x = %.2f and y = %.2f" %(x,y))#show the point of intersection ปริ้น x กับ y 