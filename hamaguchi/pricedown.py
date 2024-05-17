"""
価格表を辞書型で定義し、指定した種類の商品の価格を値下げし、値下げ後の価格表を表示するプログラム
"""
import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書くimport sys
categories = {"果物類":fruits,"酒類":alcohol,"麺類":noodles}
"""
対象のカテゴリの商品群を取得
取得した商品の価格を下げる
"""
for name in categories[hm_class]:
    if price_down > hinmoku[name]:
        hinmoku[name] = 1
    else :
        hinmoku[name] -= price_down

print(hinmoku,end="")





