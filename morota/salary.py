import sys
args = sys.argv
#四捨五入の為に、モジュールをインポート
from decimal import Decimal, ROUND_HALF_UP

#引数を変数に代入
salary = int(args[1])

#税金の計算
if salary <= 1000000:
    tax = salary * 0.1
else:
    tax = (salary - 1000000) * 0.2
    tax += 1000000 * 0.1

#税金の四捨五入の計算
tax = Decimal(str(tax)).quantize(Decimal("0"),
      rounding = ROUND_HALF_UP)

#支給額の計算
allowance = salary - tax

#表示（※+での文字列連結はstr型でないと連結できない）
print("支給額:" + str(allowance) + "、税額:" + str(tax), end="")

#formatを使用した表示方法
print("支給額:{0}、税額:{1}".format(allowance, tax), end="")