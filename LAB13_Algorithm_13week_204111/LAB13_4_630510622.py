#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab13_4
#Destructive : DESTROY LIST

def square_matrix(list_x):
    row = len(list_x)#len row
    max_col2 = 0
    #find range of square matrix
    for i in range(row):
        max_col1 = len(list_x[i])
        if(max_col1 > max_col2):
            max_col2 = max_col1

    #find max of range square
    if(row > max_col2):
        add_zero = row
    else:
        add_zero = max_col2
    #add_zero is range of square 
    #range of square are most row or col(max_col2)
    for i in range(add_zero):#add row
        try:
            while (len(list_x[i]) < add_zero):
                list_x[i].append(0)# if range of row != max of range -> get zero to it
        except(IndexError):
            list_x.append([])#add col if max range is row
            for k in range(add_zero):#add zero to fill range
                list_x[i].append(0)

def main():
        list_x = [[1, 2], [1, 2, 3], [1, 2], [1, 2], [1]]

if __name__ == "__main__":
    main()