i=int(input("Nhập i: "))
j=int(input("Nhập j: "))
k=int(input("Nhập k: "))

if i < j :
    if j < k :
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i,"j =", j,"k =", k)
