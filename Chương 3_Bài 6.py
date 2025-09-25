n=int(input("nhập một số có 2 chữ số:"))

a = n//10
b = n%10

s = ['một','hai','ba','bốn','năm','sáu','bảy','tám','chín']

if (a!=0):
    if (b!=0):
        print(s[a-1],"mươi",s[b-1])
    else:
        print(s[a-1],"mươi")
else:
    if (b!=0):
        print(s[b-1])
    else:
        print("không")

