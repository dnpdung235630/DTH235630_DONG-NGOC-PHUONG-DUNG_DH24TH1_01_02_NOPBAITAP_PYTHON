import math
xA=float(input("Nhập tọa độ x của A: "))
yA=float(input("Nhập tọa độ y của A: "))
xB=float(input("Nhập tọa độ x của B: "))
yB=float(input("Nhập tọa độ y của B: "))

def Do_Dai(xA,yA,xB,yB):
    return math.sqrt((xB-xA)**2+(yB-yA)**2)
print("độ dài đoạn thẳng: ",Do_Dai(xA,yA,xB,yB))