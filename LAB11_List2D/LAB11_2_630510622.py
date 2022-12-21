#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab11_2

def remove_row_col(list_a,row,col):
    list_b = []
    sub_list = []
    if(row < 0):#reset start first row
        row = row + len(list_a)
    if(col < 0):#reset start first colum
        col = col + len(list_a[0])
    for i in range(len(list_a)):#row = แถว
        for j in range(len(list_a[0])):#col list_a[0] because ex.is squre --> n x n
            if(j != col and i != row):#don't append row and col you input
                sub_list.append(list_a[i][j])#append list_a[i][j] except row and colum
        if(i == row):#col is not col(input) but i == row ลูปนี้เลื่อนตามแถว ถ้าไม่เข้าifด้านบนsub_listจะว่าง
            #ต้องใส่ coutinueเพื่อไม่ให้ไปบรรทัดถัดไป จะได้ไม่add list ว่างเข้าไปในlistหลัก
            #จะเข้า if นี้ต้องผ่าน if ลูปของ for j ก่อน จึงไม่ต้องคิดกรณีที่ j == col เพราะลูปเลื่อนตามแถว(i)เป็นหลัก
            continue
        list_b.append(sub_list)#get sub_list to new list
        sub_list = []#reset sub_list
    return(list_b)


def main():
    ex = [[2, 3, 4, 5], [8, 7, 6, 5], [0, 1, 2, 3]]
    row = int(input())
    col = int(input())
    print(remove_row_col(ex,row,col))

if __name__ == "__main__":
    main()