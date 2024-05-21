import sys 
args = sys.argv

#リストの生成
text = args[1].split()
num = int(args[2])

print(text[num - 1], end="")


