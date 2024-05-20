import sys
args = sys.argv

#辞書型のデータ
stations = {
    "東京":0.00, 
    "品川":6.78,
    "新横浜":25.54,
    "名古屋":342.02,
    "京都":476.31,
    "新大阪":515.35
}

#駅指定
station1 = args[1]
station2 = args[2]


try:
    #エラー検証
    d1 = stations[station1]
    d2 = stations[station2]
except KeyError:
    print("のぞみの停車駅を引数に設定してください", end="")
else:
    #２駅間の距離の算出
    distance = (d1 - d2)
    print(abs(round(distance, 2)), end="")
