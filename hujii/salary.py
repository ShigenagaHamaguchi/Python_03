from decimal import Decimal, ROUND_HALF_UP
import sys

salary = int(sys.argv[1])
B = 1000000

if salary <= B:
    tax = salary * 0.1

else:
    salary2 = salary - B
    tax = salary2 * 0.2 + B * 0.1

tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
pay = salary - tax
print("支給額:" + str(pay) + "、" + "税額:" + str(tax), end="")