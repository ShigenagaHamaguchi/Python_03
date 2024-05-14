import sys
"""
引数を取得し、int型に変換する。
その後、偶奇判定を行う。
"""
nums = list(map(lambda x:int(x),sys.argv[1:]))
p = lambda x: print(x,end="")
for num in nums:
    if num % 2 == 0:p("偶数")
    else:p("奇数")