# 630510622
# ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab02_4

#แปลงเลขmillisec เป็น แต่ละหน่วยเวลาก่อน เพื่อจะนำมาลบกับค่าของเลขที่ถูกปัด

#day hr min sec milsec
milisec = int(input("Input number of milliseconds: "))
days = milisec/(1000*60*60*24) #milisec to day หาก่อนว่าเสี้ยววิที่inputเข้ามามีค่าทั้งหมดกี่วันแล้วหน่วยอื่นๆค่อยตัดทอนตัวหารไป
#print (days)
hours = days *24#days to hours *24 เพราะ ดูว่าmilisec ได้กี่ชั่วโมง
#print(hours)
minute = hours * 60 #hours to minute *60 เพราะ ดูว่าmilisec ได้กี่นาที
#print(minute)
second = minute * 60 #minute to second *60 เพราะ ดูว่าmilisec ได้กี่วินาที
#print(second)
#-------------------------------------
#แปลงเป็นจำนวนเต็ม เพราะ จะต้องนำเลขไปลบออกให้เหลือแต่เศษ
days = int(days) #days to integer 
hours = int(hours)#hours to integer 
minute = int(minute)#minute to integer 
second = int(second)#second to integer 
#-------------------------------------
#variable to integer because the answer is an integer
#-------------------------------------
#print(milisec)
milisec = milisec - (second*1000) # เอาmilisec ค่าเต็ม ลบกับ ค่า milisec ที่ปัดเลข
#print(second)
second = second - (minute*60) # เอา second ค่าเต็ม ลบกับ ค่า second ที่ปัดเลข
#print(minute)
minute = minute - (hours*60) # เอา minute ค่าเต็ม ลบกับ ค่า minute ที่ปัดเลข
hours = hours - (days*24) # เอา hours ค่าเต็ม ลบกับ ค่า hours ที่ปัดเลข
#line 20 to 23 are process number to separate each unit
print("Results = %d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s)"%(days,hours,minute,second,milisec))#show the results