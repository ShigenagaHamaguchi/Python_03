import sys
args = sys.argv
try:
    sta1 =args[1]
    sta2 = args[2]

    stations = {
        "東京":0.00, 
        "品川":6.78,
        "新横浜":25.54,
        "名古屋":342.02,
        "京都":476.31,
        "新大阪":515.35,
    }

    result = abs(round(stations[sta2]-stations[sta1], 2))

    print(result, end="")
except KeyError:
    print("のぞみの停車駅を引数に設定してください", end="")