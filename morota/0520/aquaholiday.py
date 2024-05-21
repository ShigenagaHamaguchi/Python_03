import sys
import datetime
args = sys.argv

from datetime import date 
from database import session    # データベースへの接続
from tables import Holiday      # テーブル定義

# 料金表
# adult_prices = {"平日":2000, "土日":2400}
# child_prices = {"平日":1200, "土日":1500}

day = int(args[1])
adult = int(args[2])
child = int(args[3])

# 日付読み込み
day = datetime.datetime.strptime(sys.argv[1], "%Y%m%d")

#祝日の取得
holidaylist = session.query(Holiday.holi_date).all()

# 新しいリストを作る
holidays = []
for i in range(len(holidaylist)):
    holidays.append(holidaylist[i][0])
    i += 1

#祝日休日判定
price = 0
if day.date() in holidays:
    price = (2400 * adult) + (1500 * child)
elif day.weekday() == 5 or day.weekday() == 6:
    price = (2400 * adult) + (1500 * child)
else:
    price = (2000 * adult) + (1200 * child)

print(price, end="")