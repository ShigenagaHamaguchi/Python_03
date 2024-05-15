
import sys
# 引数から動物名とインデックスを取得
idx = int(sys.argv[1])
animal = sys.argv[2]
p = lambda x: print(x,end="")

# 配列の初期化
animals = [  "giraffe", "tiger", "zebra", "elephant", "lion"]
# 配列に挿入
animals.insert(idx,animal)
# 配列の最後の要素を削除
del animals[-1]
# 配列を昇順に並べ替え
animals.sort()

p(animals)

