import math

n=int(input("Nhập N: "))
s=0

for i in range(1,n+1,1):
    s=math.sqrt(2+math.sqrt(s))

print("Kết quả: ",s)