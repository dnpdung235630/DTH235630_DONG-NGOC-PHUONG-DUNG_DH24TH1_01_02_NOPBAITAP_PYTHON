a=int(input("Nhập số a:"))
b=int(input("Nhập số b: "))
ch=str(input("Nhập một kí tự phép tính (+ - * /): "))

if (ch=='+'):
    print("kết quả: ",a+b)
elif (ch=='-'):
    print("kết quả: ",a-b)
elif (ch=='*'):
    print("kết quả: ",a*b)
elif (ch=='/'):
    print("kết quả: ",a/b)
else:
    print(ch," không phải là một toán tử")
