import sys
args = sys.argv

def func_distance(start, goal):
    station = {"東京": 00, "品川": 6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}
    distance = round(station[goal] - station[start], 2)
    
    if distance < 0:
        distance *= -1
        print(round(distance, 2))
    else:
        print(round(distance, 2))

try:
    func_distance(args[1], args[2])
except:
    print("のぞみの停車駅を引数に設定してください")