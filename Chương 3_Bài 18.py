n=int(input("Nhập n: "))

"""for i in range(n):
    if i!=0 and i!=n-1:
        print('*     *')
    else:
        print('* * * *')

dem = n
for i in range(0,n+1,1):
    for j in range(0,n+1,1):
        if j >= dem:
            if j!=n:
                line = " *"
                print(line,end="")
            else:
                dem-=1
        else:
            line = '  '
            print(line,end="")
    print()
"""
m = n*2+1

if m%2!=0:
    mid = (m+1)/2
else:
    mid = m/2
for i in range(1,m+1,1):
    for j in range (1,m+1,1):
        if (i==mid) :
            line = " * "
            print(line,end="")
        elif (i<mid):
            if (j==1) or (i==j):
                line = " * "
                print(line,end="")
            else:
                line = "   "
                print(line, end="")
        else:
            if (j==m) or (i==j):
                line = " * "
                print(line,end="")
            else:
                line = "   "
                print(line, end="")
    print()
"""            
  1 2 3 4 5 6 7 8 9
1 *
2 * *
3 *   *
4 *     *
5 * * * * * * * * *
6           *     *
7             *   *
8               * *
9                 *

     """
