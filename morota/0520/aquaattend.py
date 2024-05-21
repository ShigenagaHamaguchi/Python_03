import sys
import datetime
args = sys.argv

from datetime import date 
from database import session    # データベースへの接続
from attendnumtable import Attendnum      # テーブル定義

#日付読み込み
day = datetime.datetime.strptime(sys.argv[1], "%Y%m%d")

#日付リスト取得
entry_data = session.query(Attendnum.entry_date).all()
#新しいリストを作る
entrylist = []
for i in range(len(entry_data)):
    entrylist.append(entry_data[i][0])
    i += 1

#同じ日付の連番追加処理
if entrylist.count(day.date()) > 0:
    seqcount = entrylist.count(day.date()) + 1
else:
    seqcount = 1

#登録するデータの編集
attendnum = Attendnum(
    entry_date = day.date(),
    seq = seqcount,
    adult = int(args[2]),
    child = int(args[3])
    )

#INSET処理
session.add(attendnum)

#コミット
session.commit()