import sys
args = sys.argv

#引数を変数に代入
num = int(args[1])
name = args[2]

#動物の名前リスト
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

#第2引数で設定したインデックスの位置に、第3引数の動物名を挿入する
animals.insert(num, name)

#リストの最後の要素を削除する
animals.pop()

#リストを昇順に並べ替える
animals.sort()

print(animals, end="")



