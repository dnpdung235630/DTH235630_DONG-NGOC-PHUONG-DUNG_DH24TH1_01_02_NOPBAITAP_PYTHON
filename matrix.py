
def TaoMaTran(m,n):
    D=[]
    for i in range(m):
        row=[]
        for j in range(n):
            so=int(input("Nhập một số: "))
            row.append(so)
        D.append(row)
    return D
def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element,end='\t')
        print()
def LayDong(r):
    R=D[r]
    return R
def XuatList1Chieu(R):
    for element in R:
        print(element,end='\t')
def LayCot(c):
    C=[]
    for i in range(len(D)):
        C.append(D[i][c])
    return C
def MAX(D):
    max=D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if(max<D[i][j]):
                max=D[i][j]
    return max
