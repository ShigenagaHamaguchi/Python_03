from database import session    # データベースへの接続
from tables import Holiday      # テーブル定義

# データを取得する
holidaylist = session.query(Holiday).all()

for holiday in holidaylist:
    print(holiday.holi_date, holiday.holi_text)
