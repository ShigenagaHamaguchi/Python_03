from decimal import Decimal,ROUND_HALF_UP
import sys

salary = int(sys.argv[1])

B = 1000000

if (salary < B) :
    tax = salary * 0.1
else :
    tax  = (salary-B)*0.2 + B*0.1
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
payamount = salary - tax
print("支給額:{}、税額:{}".format(payamount,tax),end="")

    




