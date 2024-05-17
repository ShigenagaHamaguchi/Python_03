"""
与えられた給与に対して、支払額・税額を算出し表示するプログラム
"""

from mod.func_salary import payamount_calculation
import sys

# 引数の取得
salaries = list(map(lambda x:int(x),sys.argv[1:]))
p = lambda x: print(x)

"""
引数の値から、支払額・税額を算出し表示する
"""
for salary in salaries:
    payamount,tax = payamount_calculation(salary)
    p("給与:{}、支給額:{}、税額:{}".format(salary,payamount,tax))
