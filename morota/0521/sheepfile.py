import os
import sys
args = sys.argv

#引数を変数に代入
n = int(args[1])

#相対パスの生成
path = os.path.join(".", "files", "sheep.txt")

#相対パス先のファイルを開く
file = open(path, mode="w", encoding="utf-8")

#直下のファイルを開く
#file = open("sheep.txt", mode="w", encoding="utf-8")

#ファイルにn回書き込みを繰り返す
i = 0
for i in range(n):
    i += 1
    file.write("ひつじが{}匹\n".format(i))

#ファイルを閉じる
file.close()

