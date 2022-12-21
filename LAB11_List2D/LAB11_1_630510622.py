#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab11_1
#the row times the colum
def matrix_mult(m1,m2):
    maxtrix_result = []
    sub_maxtrix = []
    result = 0
    if(len(m1[0]) != len(m2)):#matrix cannot multiply
        return None
    else:
        for i in range(len(m1)):#row change
            for j in range(len(m2[0])):#col change
                for k in range(len(m1[0])):#row and col change
                    result += m1[i][k] * m2[k][j]
                sub_maxtrix.append(result)
                result = 0
            maxtrix_result.append(sub_maxtrix)
            sub_maxtrix = []
        return maxtrix_result
    
def main():
    m2 = [[1, 2, 3],[4, 5, 6]]
    m1 = [[7, 8],[9, 10],[11,12]]
    print(matrix_mult(m1,m2))
if __name__ == "__main__":
    main()
    #input
    """user_matrix_1 = []
    user_sub_matrix_1 = []
    user_matrix_2 = []
    user_sub_matrix_2 =[]
    check_for_end_loop = None

    while True: #Create a fisrt user's matrix.
        while True:
            if check_for_end_loop == None:
                try:
                    user_sub_matrix_1.append(int(input()))
                except ValueError:
                    user_matrix_1.append(user_sub_matrix_1)
                    user_sub_matrix_1 = []
                    break
            else:
                user_sub_matrix_1.append(check_for_end_loop)
                check_for_end_loop = None

        try:
            check_for_end_loop = int(input())
        except ValueError:
            break

    while True: #Create a second user's matrix.
        while True:
            if check_for_end_loop == None:
                try:
                    user_sub_matrix_2.append(int(input()))
                except ValueError:
                    user_matrix_2.append(user_sub_matrix_2)
                    user_sub_matrix_2 = []
                    break
            else:
                user_sub_matrix_2.append(check_for_end_loop)
                check_for_end_loop = None

        try:
            check_for_end_loop = int(input())
        except ValueError:
            break
    print(matrix_mult(user_matrix_1,user_matrix_2))"""


