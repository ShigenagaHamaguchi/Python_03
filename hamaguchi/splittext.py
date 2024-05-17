import sys

"""
英文と取り出したい単語の位置を入力し
指定した位置の単語出力するプログラム
"""

#引数から対象の英文と位置を取得
texts = sys.argv[1].split(" ")
idx = int(sys.argv[2])

#指定した位置の単語を出力
print(texts[idx-1],end="")