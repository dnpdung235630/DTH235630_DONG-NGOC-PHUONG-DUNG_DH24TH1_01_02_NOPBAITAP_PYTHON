s = str(input("Nhập một chuỗi: "))

def NegativeNumberInStrings(s):
    for i in range(0, len(s), 1):
            if (s[i] == "-") and (s[i+1].isdigit()==True):
                e = i+2
                while(s[e].isdigit()):
                    e+=1
                print(s[i:e])
                i=e-1


print("các số nguyên âm trong chuỗi vừa nhập là:")
NegativeNumberInStrings(s)
