
#四捨五入の為に、モジュールをインポート
from decimal import Decimal, ROUND_HALF_UP

def calcsalary (salary):
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

    #戻り値
    return allowance, tax