import sys
num = int(sys.argv[1])
result = num

if result > 100:
    print("Over!", end="")
    

while result <= 100:
    if result == 100:
        print("Just 100!", end="")
        break
    result += num
    if result > 100:
        print("Over!", end="")
    
    
    


