import matrix

dong = int(input("Nhập số dòng: "))
cot = int(input("Nhập số cột: "))

A=[]
B=[]
S=[]

print("Nhập ma trận A: ")
for i in range(0, dong, 1):
    t=[]
    for j in range(0, cot, 1):
        so = int(input("Nhập một số: "))
        t.append(so)
    A.append(t)

print("Nhập ma trận B: ")
for i in range(0, dong, 1):
    t=[]
    for j in range(0, cot, 1):
        so = int(input("Nhập một số: "))
        t.append(so)
    B.append(t)

print("Tổng 2 ma trận: ")
for i in range(0, dong, 1):
    t=[]
    for j in range(0, cot, 1):
        t.append(A[i][j]+B[i][j])
    S.append(t)

matrix.XuatMaTran(S)