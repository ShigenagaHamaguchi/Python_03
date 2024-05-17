"""
給与から税額と支払額を算出するプログラム
"""

B = 1000000 # ボーダー

from decimal import Decimal,ROUND_HALF_UP

def payamount_calculation(salary):
    if (salary < B) : # ボーダーを下回っていた場合の税額
        tax = salary * 0.1
    else : # ボーダーを上回っていた場合の税額
        tax  = (salary-B)*0.2 + B*0.1
    
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    payamount = salary - tax
    return payamount,tax
    pass