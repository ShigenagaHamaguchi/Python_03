import sys
args = sys.argv

#引数を変数に代入
n = args[1]

#inputを使う場合↓
#n = input("整数を入力してください")

#2で割り切れたら偶数、2で割り切れなければ奇数 となる条件分岐
if int(n) % 2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")


