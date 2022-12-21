#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab11_3

def is_magic_square(board):
    checker1 = 0
    checker2 = 0
    list_b = []
    j = 0
    n = len(board)**2
    """for j in range (len(board)):#เช็คว่าในlistจำนวนสมาชิกเป็นสี่เหลี่ยมจัตุรัสมั้ย
        count += len(board[j])
    if(n != count):
        return False"""
    ## if number in magic square > len(board)**2 or have same number --> not magic square ## check in line 18 to 22
    #checker2 check row,col,diagonal are sum equal
    #checker1 check row/col/diagonal new loop 
    #if checker1 sum the same all ,let check with checker2 another row,col or diagonal
    for i in range(len(board)):#number in square <= len(board)**2
        for j in range(len(board[j])):
            if(board[i][j] in list_b or board[i][j] > n):#เลขในlistต้องไม่มากกว่า n หรือ เลขในสี่เหลี่ยมซ้ำกัน
                return False#if number in square > len(board)**2 or have same number --> not magic square
            list_b.append(board[i][j])
    for i in range (len(board)):#sum all row 
        for j in range (len(board)):
            checker1 += board[i][j]
        if(checker2 != checker1 and i != 0):#i != เพราะ เช็คดักรอบแรก checker2 มันเป็น 0 ในตอนแรก เลยไม่นับ
            return False
        checker2 = checker1
        checker1 = 0
    for i in range (len(board)):#sum all col
        for j in range(len(board)):
            checker1 += board[j][i]
        if(checker2 != checker1):
            return False
        checker1 = 0
    j = 0
    for i in range(len(board)):#sum all diagonal left up to right down
        checker1 += board[i][j]
        j += 1
    if(checker2 != checker1):
        return False
    checker1 = 0
    k = 1
    for i in range(len(board)):#sum all diagonal right up to left down
        checker1 += board[i][len(board)-k]
        k += 1
    if(checker2 != checker1):
        return False
    return True
def main():
    board = [[3,8 ,7 ],[10, 6, 2,],[5, 4, 9]]
    print(is_magic_square(board))

if __name__ == "__main__":
    main()