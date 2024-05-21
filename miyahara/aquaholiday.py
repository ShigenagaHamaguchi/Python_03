import sys
from datetime import date
import datetime

# 祝日データの取り込み
from database import session
from tables import Holiday

holiday2 = []

holidaylist = session.query(Holiday).all()
for holiday in holidaylist:
    holiday2.append(holiday)
    

# データの入力
date = sys.argv[1]
count_adult = int(sys.argv[2])
count_child = int(sys.argv[3])

year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8]) 

dt = datetime.date(year, month, day)
strftime = dt.strftime("%a")

holiday1 = ["Sat","Sun"]



if(strftime in holiday1 and dt in holiday2):
    adult_fee = 2400
    child_fee = 1500
else:
    adult_fee = 2000
    child_fee = 1200

count = adult_fee * count_adult + child_fee * count_child
print(count, end="")