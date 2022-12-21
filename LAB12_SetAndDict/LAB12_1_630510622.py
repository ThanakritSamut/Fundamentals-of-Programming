#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab12_1
import string
def sort_date(list_x):
    index = 0
    slash = "/"
    for i in list_x:#split the day month year #--> ["11","1","2100"]
        list_x[index] = i.split("/")
        index += 1#split all index

    for i in list_x:#list_x after split with "/"
        for j in range (len(i)):
            i[j] = int(i[j])#change str to int for compare
    for i in list_x:
        i[0],i[2] = i[2],i[0]#Switch position day and year #get year index[0] be easy to sorted
    list_x.sort()#sorted
    # get back to old form # add slash,change to str
    for i in list_x:
        for j in range (len(i)):
            i[j] = str(i[j])#get all index  to string
    for i in list_x:
        i[0],i[2] = i[2],i[0]#Switch back to old positon
    for i in range(len(list_x)):
        list_x[i] = slash.join(list_x[i])#get "/" between date

def main():
    list_x = ["11/1/2013","5/12/2013","19/1/2013","11/9/2013"]
    sort_date(list_x)
    print("---")
    print(list_x)
if __name__ == "__main__":
    main()