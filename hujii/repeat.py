import sys
args = sys.argv

total = int(args[1])

while total < 100:
    total += total

else:
    if total == 100:
      print("Just 100!")

    else:
      print("Over!")
    