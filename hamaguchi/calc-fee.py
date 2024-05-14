

children = int(input("子供何人: "))
normal = int(input("通常何人: "))
elder = int(input("年配者何人: "))

total_num = children + normal + elder

children_price = 500 * children
normal_price = normal * 1000
elder_price = elder * 700

total_price = children_price + normal_price + elder_price

if total_num >= 10:
    print("団体割引があります")
    total_price *= 0.8
else :
    print("割引はありません")

print("子供: {}人 子供料金: {}円".format(children,children_price))
print("大人: {}人 大人料金: {}円".format(normal,normal_price))
print("老人: {}人 老人料金: {}円".format(elder,elder_price))
print("トータル: {}人 トータル: {}円".format(total_num,int(total_price)))
