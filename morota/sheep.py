import sys
args = sys.argv

#引数を変数に代入
n = int(args[1])

#n回表示を繰り返す
i = 0
for i in range(n):
    i += 1
    print("ひつじが{}匹".format(i))