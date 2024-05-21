from holiday_list import insert_holiday,count_attendnum
from attendnum import Attendnum
import datetime
import sys
def insert_attend_num(day,adult,children):
    # 同じ日のカウント
    count = count_attendnum(day.date())
    # seqの値に1を追加して挿入
    insert_holiday(Attendnum(entry_date=day.date(),seq=count+1,adult=int(adult),child=int(children)))


day = datetime.datetime.strptime(sys.argv[1],"%Y%m%d")
adult = int(sys.argv[2])
children = int(sys.argv[3])
insert_attend_num(day,adult,children)




