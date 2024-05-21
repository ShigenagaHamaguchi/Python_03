import sys
import os
sheep_num = int(sys.argv[1])
path = os.path.join(".","files","sheeps.txt")
with open(path,mode="w") as w:
    for i in range(1,sheep_num+1):
        w.write("ひつじが{}匹\n".format(i))