day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

def Nam(int year):
    print("1/1/",(year+1))

def Thang(int month,int year):
    print("1/",(month+1),"/",year)

def Ngay(int day,int month,int year):
    print((day+1),"/",month,"/",year)

def NamNhuan(int year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if (month in (1,3,5,7,8,10,12)):
    if (day == 31 and month == 12):
        Nam(year)
    elif (day==31 and month != 12):
        Thang(month,year)
    else:
        Ngay(day,month,year)

if (month in (4,6,9,11)):
    if (day == 30):
        Thang(month,year)
    else:
        Ngay(day,month,year)

if (month == 2):
    if (Nam)