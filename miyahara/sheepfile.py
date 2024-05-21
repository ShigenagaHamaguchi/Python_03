import sys
import os
args = int(sys.argv[1])

path = os.path.join("..", "..","files","sheep.txt")

with open(path, mode="w", encoding="utf-8") as f:
        for i in range(1, args+1):
            f.write("ひつじが{}匹".format(i))
