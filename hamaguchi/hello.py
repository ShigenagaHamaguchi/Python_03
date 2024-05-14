import sys

args = sys.argv

if "-h" in args:
    print("hello world")
elif "-i" in args:
    hello = input()
    print(hello)