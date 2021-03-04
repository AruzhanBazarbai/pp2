def f_write(fname):
    with open(fname,"w") as f:
        f.write("11111111\n")
        f.write("22222222\n")
    txt=open(fname,"r")
    print(txt.read())
f_write("abs.txt")
