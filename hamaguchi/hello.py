import sys

args = sys.argv
print(sys.path)
if "-h" in args:
    print("hello world")
elif "-n" in args:
    name = input()
    print("Hello",name)