n=int(input("Nhập số lượng phần tử của mảng: "))

list = []
for i in range(0, n, 1):
    m = float(input("Nhập một số thực: "))
    list.append(m)

list.sort(reverse=True)
print(list)