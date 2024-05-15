from decimal import Decimal, ROUND_HALF_UP
import sys

args = sys.argv

salary = int(args[1])
base = 1000000

if(salary <= base):
    tax = salary * 0.1
else:
    tax = (salary - base)*0.2 + base*0.1

tax = Decimal(str(tax)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)

payamount = salary - tax
print("支給額:{}、税額:{}".format(payamount,tax),end="")
