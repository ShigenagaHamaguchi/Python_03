"""
第2引数に日付（YYYYMMDD形式）、
第3引数に大人の人数、
第4引数に子供の人数を渡すと、
平日か土日かにより料金を算出し、合計金額を計算して出力するプログラム
"""
import sys
import datetime
from holiday_list import get_holidays
#初期値の設定
WEEKEND = [0,6]
ADULT_PRICE = [2000,2400]
CHILDREN_PRICE = [1200,1500]

# 引数の取得
day = datetime.datetime.strptime(sys.argv[1], "%Y%m%d")
adult = int(sys.argv[2])
children = int(sys.argv[3])
holidays = get_holidays()
print(holidays)
print(day)
# 週末判定
if int(day.strftime('%w')) in  WEEKEND or day.date() in holidays:
    print("祝")
    adult_price = adult*ADULT_PRICE[1]
    children_price = children*CHILDREN_PRICE[1]
else:
    adult_price = adult*ADULT_PRICE[0]
    children_price = children*CHILDREN_PRICE[0]

print(adult_price+children_price,end="")



