import os
def read():
    current_path=os.getcwd()
    print(current_path)
    with open(os.path.join(current_path,"folder1/input.txt"),'r') as f:
        line=f.readline()
        nums=line.split()
        cnt=0
        for num in nums:
            cnt+=int(num)
        print(cnt)
read()
