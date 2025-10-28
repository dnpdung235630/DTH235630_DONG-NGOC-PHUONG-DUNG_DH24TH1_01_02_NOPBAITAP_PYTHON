n = int(input("Nhập số lượng phần tử của mảng:"))

list = []
for i in range(0,n,1):
    m = int(input("Nhập một số: "))
    for j in range(0, len(list), 1):
        if m < list[j]:
            m = int(input("Nhập lại số lớn hơn: "))

    list.append(m)

print(list)