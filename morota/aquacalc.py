import sys
import datetime
args = sys.argv

# 料金表
# adult_prices = {"平日":2000, "土日":2400}
# child_prices = {"平日":1200, "土日":1500}

day = int(args[1])
adult = int(args[2])
child = int(args[3])

date = datetime.datetime.strptime()

# price = 0
# if .weekday()
#     price = (2400 * adult) + (1500 * child)
# else:
#     price = (2000 * adult) + (1200 * child)

# print(price, end="")