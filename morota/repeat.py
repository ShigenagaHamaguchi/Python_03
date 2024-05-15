import sys
args = sys.argv

#引数を変数に代入
n = int(args[1])

total = 0
#足し算の合計が100になるまで繰り返す
while total < 100:
        total += n
else:
    if total == 100:
         print("Just 100!", end="")
    elif total > 100:
         print("Over!", end="")

