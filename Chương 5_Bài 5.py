import string

"""https://toidicode.com/cac-ham-xu-ly-chuoi-trong-python-368.html"""
s = str(input("Nhập một chuỗi: "))
dem_in_hoa = 0
dem_in_thuong = 0
dem_so = 0
dem_space = 0
dem_khac = 0
for i in s:
    if (i.isupper()==True):
        dem_in_hoa+=1
    elif (i.islower()==True):
        dem_in_thuong+=1
    elif (i.isdigit()==True):
        dem_so+=1
    elif (i.isspace()==True):
        dem_space+=1
    else:
        dem_khac+=1

print("thống kê chuỗi bao gồm:")
print("chữ in hoa: ",dem_in_hoa)
print("chữ in thường:",dem_in_thuong)
print("chữ số:",dem_so)
print("ký tự đặc biệt:",dem_khac)
print("khoảng trắng:",dem_space)

