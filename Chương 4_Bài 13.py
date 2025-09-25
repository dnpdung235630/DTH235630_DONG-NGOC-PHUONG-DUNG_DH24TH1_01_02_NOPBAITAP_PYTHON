n=int(input("Nhập số N: "))

while n<=0:
    n=int(input("Nhập lại số N: "))

def So_Hoan_Thien(n):
    s = 0
    for i in range(1,n,1):
        if n % i == 0:
            s+=i
    if (s==n):
        return 1
    elif (s>n):
        return -1
    else:
        return 0

i=So_Hoan_Thien(n)
if i==1:
    print(n,"là số hoàn thiện")
elif i==-1:
    print(n,"là số thinh vượng")
else:
    print(n,"không phải là 1 trong 2 loại số trên")



