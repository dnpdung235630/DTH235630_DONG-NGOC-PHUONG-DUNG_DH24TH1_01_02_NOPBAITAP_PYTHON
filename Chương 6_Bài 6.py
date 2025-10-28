n = int(input("Nhập số lượng phần tử của mảng:"))

list = []
for i in range(0, n, 1):
    m = int(input("Nhập một số: "))
    while m in list:
        m = int(input("Nhập lại số khác:"))
    list.append(m)

print(list)
