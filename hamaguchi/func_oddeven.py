import sys
"""
引数を取得し、int型に変換する。
その後、偶奇判定を行う。
"""

def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

nums = list(map(lambda x:int(x),sys.argv[1:]))

for num in nums:
    calcvalue(num)


