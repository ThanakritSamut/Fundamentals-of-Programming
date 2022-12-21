#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab12_2

def search_event(list_x,key):#find EVENT with key
    result = key.split("/")#split "/" for strip left zero of day (line 10)
    index = 0
    for i in result:
        result2 = i.lstrip("0")#01 and 1 is same date get left zero out
        result[index] = result2#get day without left zero
        index += 1
    count = len(result)
    row = 0
    useful = ""
    for j in result:#get "/" back for check key in dict (line 21)
        useful += j#useful = day or month
        row += 1#for get "/" between 
        if(row < count):
            useful += "/"
    list_x = dict(list_x)#get list_x to dict to  call key
    if(useful in list_x):#useful is key
        Event = list_x[useful]#get Event (value)
        return (useful,Event)#return key and Event
    else:
        return None
def main():
    list_x =[("1/1/1900","Event A"),("5/12/2001","Event B"),
    ("5/12/2002","Event C"),("20/8/2000","Event D"),("9/3/2013","Event E"),
    ("11/3/2017","Event F"),("7/5/2019","Event G"),("29/2/2032","Event H"),("9/11/2042","Event I")]
    key = input()
    event = search_event(list_x,key)
    print("---")
    print(event)
if __name__ == "__main__":
    main()