import sys
# 引数を取得
num = int(sys.argv[1])
p = lambda x: print(x,end="")
# 合計値の初期化
sum = 0
"""
引数を100以上になるまで足し続ける。
100ならJust 100,100以上ならOverを出力
"""
while True:
    if sum == 100:
        p("Just 100")
        break
    elif sum > 100:
        p("Over!")
        break
    sum += num

