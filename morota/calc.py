import sys
args = sys.argv

#引数を変数に代入
input1 = args[1]
input2 = args[2]
input3 = args[3]

#文字列をint型に変換して計算する
total = int(input1) + int(input2) + int(input3)
print(total, end="")