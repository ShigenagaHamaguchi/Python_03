import sys
p = lambda x: print(x,end="")

start = sys.argv[1]
target = sys.argv[2]

distances = {"東京":0.0, "品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35 }

distance = distances[target] - distances[start]

p("{}".format(abs(round(distance,2))))

