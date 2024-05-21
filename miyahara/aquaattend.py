import sys
from datetime import date
import datetime

# 祝日データの取り込み
from database import session
from tables import Attendnum

# データの入力
date = sys.argv[1]
count_adult = int(sys.argv[2])
count_child = int(sys.argv[3])

year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8]) 

dt = datetime.date(year, month, day)

# 入力値の日の連番を確認して、値が空ではなかったら

attendget = session.query(Attendnum).filter_by(entry_date = dt).order_by(Attendnum.seq.desc()).first()

if attendget != None:
    seq = attendget.seq + 1
else:
    seq = 1

# 値の入力

attendnum = Attendnum(
    entry_date = dt,
    seq = seq,
    adult = count_adult,
    child = count_child
)

session.add(attendnum)
session.commit()