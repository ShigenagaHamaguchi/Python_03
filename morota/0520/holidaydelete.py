from datetime import date 
from database import session    # データベースへの接続
from tables import Holiday      # テーブル定義

# 削除するデータの取得
result = session.query(Holiday).filter_by(holi_date=date(2023, 1, 1)).delete()

# コミット
session.commit()