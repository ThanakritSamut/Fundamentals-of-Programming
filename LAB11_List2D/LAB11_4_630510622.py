#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab11_4

def sum_nested_list(list_a):
    n = len(list_a)
    list_b = []
    result = 0
    i = 0
    while i != len(list_a):#if i == len --> all index are extend
        if(isinstance(list_a[i],int)):#ถ้าเจอเลขในlistก็ปล่อยผ่านไปถ้าไม่ใช่เข้าelseเพื่อแยก[]ออกมาให้เป็นint
            pass
        else:#get [] out
            list_a.extend(list_a[i])
        i += 1
    list_b.append(list_a)#get list_a to list_b 
    list_b.extend(list_b[0])#change list_b same list_a
    del(list_a[n:])#get list_a to first form
    for j in range(len(list_b)):#sum all int in list_b
        if(isinstance(list_b[j],int)):
            result += list_b[j]
    return result

def main():
    list_a = [81, [[31, [159]], 9577, [22, [181, [41]]]]]
    print(sum_nested_list(list_a))

if __name__ == "__main__":
    main()