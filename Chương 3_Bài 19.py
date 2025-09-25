x=int(input("Nhập x: "))
n=int(input("Nhập N: "))
def Nhap():
    x=int(input("Nhập x: "))
    n=int(input("Nhập N: "))

if (x<0) or (n<0):
    Nhap()
tu = 1
mau = 1
for i in range(1,2*n+2,2):
    tu*=x
    for j in range(2,i+1,2):
        mau*=j

print("s({0},{1})={2}".format(x,n,tu/mau))