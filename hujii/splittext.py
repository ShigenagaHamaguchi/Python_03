import sys
args = sys.argv

text = str(args[1])
num =  int(args[2])

#文字列を分割
word = text.split()
print(word[num-1])