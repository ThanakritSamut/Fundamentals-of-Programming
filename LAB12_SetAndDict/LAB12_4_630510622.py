#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab12_4

def list_to_list(p):
    lst = dict()
    sub_list = []
    llst = []
    #sum number same power x
    for i in p:
        if(i[0] not in lst):
            lst[i[0]] = i[1]
        else:
            lst[i[0]] += i[1]
    for i in lst:#get back to tuple after sum same power x
        sub_list.append(i)#2x^3 get x (3)
        sub_list.append(lst[i])#2x^3 get number (2) 
        llst.append(tuple(sub_list))#get back to tuple
        sub_list = []
    return(llst)
def polynomial_addition(p1,p2):
    sub_list = []
    list_result = []
    p1 = list_to_list(p1)
    p2 = list_to_list(p2)
    list_result = []
    #================ equation = none ======================#
    if(p1 == []):
        return p2
    elif(p2 == []):
        return p1
    for i in p1:
        for j in p2:
            if(i[0] != j[0]):
                checker = False
            else:
                checker = True
                break
        if(checker == False and i[1] != 0):
            list_result.append(i)
    for j in p2:
        for i in p1:
            if(j[0] != i[0]):
                checker = False
            else:
                checker = True
                break
        if(checker == False and j[1] != 0):
            list_result.append(j)
    #================ equation = none ======================#

    #sum equation
    for i in p1:
        for j in p2:
            if i[0] == j[0]:#if power of x of two equation the same sum it
                if(i[1] + j[1] == 0):#if number = 0 don't get to list because result = 0
                    #use continue to get next power of x
                    continue
                sub_list.append(i[0])#get x to list
                sub_list.append(i[1] + j[1])#sum number and get it to list
        sub_list = tuple(sub_list)#change to tuple
        if(sub_list != ()):#some equation result are none -> (),don't get it
            list_result.append(sub_list)
        sub_list = []#clear sub_list for next compare 
    return sorted(list_result,reverse=True)#list_result form Descending
def main():
    p1 = [(99, 3), (95, 20)]
    p2 = []
    print(polynomial_addition(p1,p2))
if __name__ == "__main__":
    main()