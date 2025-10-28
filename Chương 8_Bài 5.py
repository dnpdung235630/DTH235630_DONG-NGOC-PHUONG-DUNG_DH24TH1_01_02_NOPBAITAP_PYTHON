from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Enter New Password')
root.geometry('450x300')

def clicked_OK():
    s_old = txtOldPass.get()
    s_new_1 = txtNew1.get()
    s_new_2 = txtNew2.get()
    if ((s_old == s_new_1) or (s_old == s_new_2)):
        messagebox.showerror("Thông báo","Bạn không được dùng mật khẩu cũ")
    elif (s_new_1 != s_new_2):
        messagebox.showerror("Thông báo","Bạn phải nhập lại mật khẩu mới giống nhau")
    else:
        messagebox.showinfo("Thông báo","Thành công")

def clicked_Cancel():
    root.quit()
txtOldPass = Entry(root,show ='*')
txtOldPass.grid(row =0,column=1)
txtNew1 = Entry(root,show ='*')
txtNew1.grid(row=1,column=1)
txtNew2 = Entry(root,show ='*')
txtNew2.grid(row=2,column=1)

Label(root,text ='Old Password:',justify = LEFT).grid(row=0,column=0)
Label(root,text = 'New Pasword:',justify = LEFT).grid(row=1,column=0)
Label(root,text = 'Enter New Password Again:',justify = LEFT).grid(row=2,column=0)

frmButton = Frame(root)
btnOk = Button(frmButton,text = 'OK',command = clicked_OK).pack(side = LEFT)
btnCancel = Button(frmButton,text = 'Cancel',command = clicked_Cancel).pack(side = LEFT)
frmButton.grid(row=3,column=0,columnspan=2)

txtOldPass.focus()
root.mainloop()