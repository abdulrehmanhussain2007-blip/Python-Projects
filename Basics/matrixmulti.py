a_rows=0
a_cols=0
b_rows=0
b_cols=0
a_mat=list()
b_mat=list()
a_rows=int(input('Enter no. of rows'))
a_cols=int(input('Enter no. of columns'))
b_rows=int(input('Enter no. of rows'))
b_cols=int(input('Enter no. of columns'))
n=0
if a_cols!=b_rows:
    print(f"matrix cannot be multiplied because matrix a columns{a_cols} is not equal to matrix b rows {b_rows}")