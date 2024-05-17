import sys
args = sys.argv
start = str(args[1])
goal = str(args[2])

station = {"東京": 00, "品川": 6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}
distance = round(station[goal] - station[start], 2)

if distance < 0:
    distance *= -1
    print(distance)
else:
    print(distance)
