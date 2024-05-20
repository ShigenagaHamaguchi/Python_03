import sys
from datetime import date
import datetime

date = sys.argv[1]
count_adult = int(sys.argv[2])
count_child = int(sys.argv[3])

year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])

dt = datetime.date(year, month, day)
strftime = dt.strftime("%a")

holiday = {"Sat","Sun"}

if(strftime in holiday):
    adult_fee = 2400
    child_fee = 1500
else:
    adult_fee = 2000
    child_fee = 1200

count = adult_fee * count_adult + child_fee * count_child
print(count, end="")