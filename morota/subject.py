import sys
args = sys.argv

#引数を変数に代入
math = int(args[1])
japanese = int(args[2])
english = int(args[3])


if (math >= 50) and (japanese >= 50) and (english >= 50):              #1科目も50点未満がない
    if (math >= 70) and (japanese >= 70) and (english >= 70):       #3教科とも70点以上
        print("合格", end="")
    elif math + japanese + english >= 220:                          #合計点数が220点以上
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")