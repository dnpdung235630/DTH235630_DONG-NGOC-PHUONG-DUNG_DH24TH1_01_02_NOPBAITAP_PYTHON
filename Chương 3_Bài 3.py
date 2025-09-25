import math

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

delta = b**2 - 4*a*c
if delta<0:
    print("phương trình vô nghiệm")
elif delta==0:
    print("phương trình có nghiệm kép x1=x2=",-b/2*a)
else:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("phương trình có 2 nghiệm phân biệt: x1=",x1," x2=",x2)