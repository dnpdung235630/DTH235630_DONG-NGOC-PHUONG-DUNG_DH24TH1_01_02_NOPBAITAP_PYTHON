from tkinter import *

root = Tk()
root.geometry('150x300')
txtHienthi = Entry(root)
txtHienthi.grid(row=0,column=0)
def Nhap_so(n):
    s = txtHienthi.get()
    txtHienthi.delete(0,END)
    txtHienthi.insert(0,s+str(n))
    

#tạo các nút số
#frameButton.grid(row=1,column=0,rowspan=4)

frm123 = Frame(root)
for i in range(1,4,1):
    Button(frm123,text = str(i),command = Nhap_so(i)).pack(side = LEFT)
frm123.grid(row = 1,column = 0,columnspan = 3)

frm456 = Frame(root)
for i in range(4,7,1):
    Button(frm456,text = str(i),command = Nhap_so(i)).pack(side = LEFT)
frm456.grid(row = 2,column=0,columnspan=3)
frm789 = Frame(root)
for i in range(7,10,1):
    Button(frm789,text = str(i),command = Nhap_so(i)).pack(side = LEFT)
frm789.grid(row = 3,column = 0, columnspan = 3)
frm4 = Frame(root)
Button(frm4,text = '_').pack(side = LEFT)
Button(frm4,text = '0',command = Nhap_so(0)).pack(side = LEFT)
Button(frm4,text = '.').pack(side = LEFT)
frm4.grid(row=4,column=0,columnspan=3)
frmToantu = Frame(root)
for i in ['+','-','*','/']:
    Button(frmToantu,text = i,command = Nhap_so(i)).pack(side = LEFT)
frmToantu.grid(row=5,column=0,columnspan=5)

def Tinh():
    kq = eval(txtHienthi.get())
    txtHienthi = str(kq)

Button(frmToantu,text = '=',command = Tinh).pack(side = LEFT)

def Xoa():
    txtHienthi.delete(0,END)
    txtHienthi.focus()

Button(root,text = 'Clr',command = Xoa).grid(row = 6,column=0,columnspan=3)

txtHienthi.delete(0,END)

root.mainloop()
