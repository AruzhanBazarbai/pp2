import os
import os.path

dir_path=os.getcwd()
print(dir_path)
print(os.path.abspath(dir_path))
print(os.path.basename(dir_path))
print(os.path.dirname(dir_path))
print(os.path.getatime(dir_path))
print(os.path.getmtime(dir_path))
print(os.path.isabs(dir_path))
print(os.path.isdir(dir_path))
print(os.path.isfile(dir_path))
print(os.path.split(dir_path))
print(os.listdir(dir_path))

# d=int(input("1.Input-back. Input:   "))
# print(d)

