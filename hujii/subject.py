import sys
args = sys.argv

#引数を変数に代入
math = int(args[1])
japanese = int(args[2])
english = int(args[3])
total = math + japanese + english

if math >= 70 and japanese >= 70 and english >= 70 and total >= 220:
    print("合格")
elif math >= 51 and japanese >= 51 and english >= 51:
    print("合格")
else:
    print("不合格")

