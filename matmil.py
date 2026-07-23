a_rows=int(input('Enter no. of rows'))
a_cols=int(input('Enter no. of columns'))
b_rows=int(input('Enter no. of rows'))
b_cols=int(input('Enter no. of columns'))
if a_cols!=b_rows:
    print(f"matrix cannot be multiplied because matrix a columns{a_cols} is not equal to matrix b rows {b_rows}")
else:
    #A
    A=[]
    for i in range(a_rows):
        row=[]
        for j in range(a_cols):
            values=int(input(f"values of A{i} and A{j} = "))
            row.append(values)
            A.append(row)
    print("A matrix will become")
    for i in range(a_rows):
        print("[",end=" ")
        for j in range(a_cols):
            print(A[i][j],end=" ")
        print("\b]")
    #B
    B=[]
    for i in range(b_rows):
        row=[]
        for j in range(b_cols):
            values=int(input(f"values of B{i} and B{j} = "))
            row.append(values)
            B.append(row)
    print("B matrix will become")
    for i in range(b_rows):
        print("[",end=" ")
        for j in range(b_cols):
            print(B[i][j],end=" ")
        print("\b]")
    #C
    C=[]
    for i in range(a_rows):
        row=[]
        for j in range(b_cols):
            row.append(0)
            C.append(row)
    #Multilication
    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(a_cols):
                C[i][j]+=A[i][k]*B[k][j]
    print("C matrix will become")
    for i in range(a_rows):
        print("[",end=" ")
        for j in range(b_cols):
            print(C[i][j],end=" ")
        print("\b]")