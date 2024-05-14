import sys



subjects = list(map(lambda x:int(x),sys.argv[1:]))
p = lambda x: print(x,end="")


# 合計判定
def bordur1(l):
    if (sum(l)<220):return False
    return True
# ボーダー判定
def bordur(l):
    for ll in l:
        if 70 > ll:return False
    return True
# ５０未満判定
def bordur2(l):
    for ll in l:
        if ll < 50: return False
    return True

if ((bordur(subjects) or bordur1(subjects)) and bordur2(subjects)):
    p("合格")
else:
    p("不合格")