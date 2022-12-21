#Destructive เปลี่ยนlistเดิม
def square_matrix(list_x):
    row = len(list_x)
    max_col2 = 0
    sub_list = []
    list_result2 = []
    #find range of square matrix
    for i in range(row):
        max_col1 = len(list_x[i])
        if(max_col1 > max_col2):
            max_col2 = max_col1
    if(row > max_col2):
        add_zero = row
    else:
        add_zero = max_col2
    #add_zero is range of square 
    #range of square are most row or col(max_col2)
    for i in range(add_zero):#add row
        try:
            sub_list = []
            sub_list.extend(list_x[i])
            for j in range (abs(len(list_x[i]) - add_zero)):#add col
                sub_list.append(0)
            list_result2.append(sub_list)
        except(IndexError):
            for k in range(add_zero):
                sub_list.append(0)
            list_result2.append(sub_list)
    #print(list_x) #check destructive
    list_x = list_result2
    return list_x


def main():
    list_x = [[1, 2],[1, 2, 3],[1, 2],[1, 2],[1]]
    print(square_matrix(list_x))

if __name__ == "__main__":
    main()