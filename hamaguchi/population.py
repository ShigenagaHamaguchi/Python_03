import sys
p = lambda x: print(x,end="")

# 順位を引数から取得
rank = int(sys.argv[1])
# 人口のランキング
cuntries = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

# 任意の順位の国を出力
p(cuntries[rank-1])