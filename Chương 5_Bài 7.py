import ToiUu

s = str(input("Nhập một chuỗi: "))

s = ToiUu.ToiUuChuoi(s)
s = s.title()


start = 0
for i in range(1, len(s), 1):
    if s[i]==" ":
        for j in range(start+1, i, 1):
            if (s[j].isupper()):
                s[j].swapcase()
        start=j
    if (i==len(s)-1):
        for j in range(start+1, len(s), 1):
            if (s[j].isupper()):
                s[j].swapcase()

print(s)


