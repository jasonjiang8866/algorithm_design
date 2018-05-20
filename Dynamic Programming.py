def faster_pascal(row, col):
    DP_table=[]
    for row_num in range(0,row):
        current_row=[]
        for col_num in range(0,row_num+1):
            if col_num==0 or col_num==row_num:
                current_row.append(1)
            else:
                current_row.append(DP_table[row_num-1][col_num-1]+DP_table[row_num-1][col_num])
        DP_table.append(current_row)
    return DP_table[row-1][col-1]
            
            
print(
faster_pascal(500, 3)
    )
