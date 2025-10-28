f = open("demofile.txt")
f = open("D:\\myfiles\welcome.txt")
print(f.read())


with open("demofile.txt") as f:
    print(f.read())
    """chỉ đọc được 1 dòng trong file và có bao nhiêu dòng thì đọc được bấy nhiêu dòng"""
    print(f.readline())


    with open("demofile.txt") as f:
        for x in f:
            """đọc hết các dòng trong file"""
            print(x)


with open("demofile.txt") as f:
  print(f.read(5))
  """chỉ in 5 kí tự đầu tiên"""

"""viết và mở rộng nên file phải được tại từ trước vì vậy không được có lệnh x để tạo file được"""
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
  """thêm câu Now the file has more content! vào cuối file"""

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

with open("demofile.txt") as f:
  print(f.read())
  """mở và đọc sau khi được append và overwrite"""

"""lệnh tạo file"""
f = open("myfile.txt","x/w/a")

import os
"""lệnh kiểm tra file có tồn tại hay không"""
if os.path.exists("demofile.txt"):
    """xóa file"""
    os.remove("demofile.txt")
    """xóa thư mục chứa file"""
    os.rmdir("demofile.txt")

else:
  print("The file does not exist")


f.close()