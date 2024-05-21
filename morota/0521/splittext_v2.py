# 問１２英文のn番目の単語は？

import sys 
args = sys.argv

# 英文を分割してリストに格納する
text = args[1].split()

# n番目の単語の出力
print(text[int(args[2]) - 1], end="")



