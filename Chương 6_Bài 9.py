n=int(input("Nhập số lượng của mảng: "))

list = []

for i in range(0,n,1):
    m = int(input("Nhập một số:"))
    list.append(m)

def KiemTraNguyenTo(n):
    for i in range(2,n,1):
        if n % i == 0:
            return False
    return True
chan = []
le = []
ngto = []
khong_ngto = []

for i in range(0,n,1):
    if list[i] % 2 == 0:
        chan.append(list[i])
    else:
        le.append(list[i])
    if (KiemTraNguyenTo(list[i])):
        ngto.append(list[i])
    else:
        khong_ngto.append(list[i])

print(chan, "->", len(chan),"số chẵn")
print(le, "->", len(le),"số lẻ")
print(ngto, "->", len(ngto),"số nguyên tố")
print(khong_ngto, "->", len(khong_ngto),"số không phải là số nguyên tố")