import sys
args = sys.argv
num = int(args[1])

#人口のランキング
cuntries = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

#引数に渡された順位を表す数字に対応する国を表示
print(cuntries[num-1])