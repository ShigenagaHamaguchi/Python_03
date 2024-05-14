import sys
p = lambda x: print(x,end="")
nums = list(map(lambda x:int(x),sys.argv[1:]))

for num in nums:
    if num % 2 == 0:p("偶数")
    else:p("奇数")
