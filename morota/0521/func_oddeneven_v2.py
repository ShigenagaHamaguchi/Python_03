# 問１４複数の整数の奇数・偶数を判定しよう

import sys
args = sys.argv

# 関数を定義
def calcvalue(num):
    # ２で割ったあまりを算出
    mod = int(num) % 2

    # 奇数偶数判定
    if mod != 0:
        print(num + "は奇数")
    else:
        print(num + "は偶数")  

# 引数を順に取り出して関数を実行
for i in args[1:]:
    calcvalue(i)

