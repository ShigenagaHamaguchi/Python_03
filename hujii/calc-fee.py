#ある遊園地の入場を計算するプログラム
#人数の入力
children = int(input("子供料金(13才未満)は何人 ? "))
normal = int(input("子供料金(13才未満)は何人 ? "))
elder = int(input("子供料金(13才未満)は何人 ? "))
#集計
total_num = children + normal + elder
children_price = children * 500
normal_price = elder * 1000
elder_price = elder * 700
total_price = children_price + normal_price + elder_price
#　割引対象か確認
if total_num >= 10:
    print("団体割引があります")
    total_price = total_price * 0.8
else:
    print("割引はありません")
#結果を表示
print("子供料金 :{0}人× 500= {1}円".format(children, children_price))