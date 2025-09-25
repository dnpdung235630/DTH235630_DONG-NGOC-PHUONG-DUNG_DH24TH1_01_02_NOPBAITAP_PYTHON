import math

a=float(input("Nhập a: "))
x=float(input("Nhập x: "))

if (a<0) or (a==1):
    a=float(input("Nhập a: "))
if (x<0):
    x=float(input("Nhập x: "))

print("kết quả: ",math.log(x,a))