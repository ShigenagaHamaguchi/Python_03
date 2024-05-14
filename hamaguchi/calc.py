import sys

"""
CLIの引数から数字を取得しintに変換。
変換したものの合計を出力
"""
args = list(map(lambda x:int(x),sys.argv[1:]))
print(args[0]+args[1]+args[2])