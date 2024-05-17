"""


"""

B = 1000000

from decimal import Decimal,ROUND_HALF_UP

def payamount_calculation(salary):
    if (salary < B) :
        tax = salary * 0.1
    else :
        tax  = (salary-B)*0.2 + B*0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    payamount = salary - tax
    return payamount,tax
    pass