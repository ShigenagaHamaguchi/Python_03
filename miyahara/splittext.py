import sys
words = sys.argv[1]
num = int(sys.argv[2])

word_li = words.split()
print(word_li[num-1], end="")

