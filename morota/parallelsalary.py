import sys
import funk_salary
args = sys.argv

# 繰り返し
for salary in args[1:]:
    allowance, tax = funk_salary.calcsalary(int(salary))
    print("支給額:{0}、税額:{1}".format(allowance, tax))    #formatを使用した表示方法
