# import sys
# args = sys.argv

# math = int(args[1])
# japanese = int(args[2])
# english = int(args[3])
# sum = math + japanese + english

# if((math >= 70 and japanese >= 70 and english >= 70) or (sum >= 220)) and (math >= 51 and japanese >=51 and english >= 51):
#     print("合格", end="")
# else:
#     print("不合格", end="")

import sys
args = sys.argv

math = int(args[1])
japanese = int(args[2])
english = int(args[3])


if (math >= 50) and (japanese >= 50) and (english >= 50):
    if (math >= 70) and (japanese >= 70) and (english >= 70):
        print("合格", end="")
    elif math + japanese + english >= 220: 
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")
