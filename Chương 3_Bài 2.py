month=int(input("nhập số tháng (1-12):"))

#tháng có 31 ngày
a = [1,3,5,7,8,10,12]
#tháng có 30 ngày
b = [4,6,9,11]

def find_day(m):
    for i in a:
        if i == m:
            return 31

    for i in b:
        if i == m:
            return 30

    if m == 2:
        year = float(input("nhập số năm: "))
        if year % 4 == 0:
            return 29
        else:
            return 28

day = find_day(month)
print("số ngày của tháng ",month," là: ",day)
