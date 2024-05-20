import sys
args = sys.argv

#タプルに【世界人口ランキング（2021年時点）】を定義
ranking = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

#引数を変数に代入しつつ計算
rank = int(args[1]) - 1

print(ranking[rank], end="")