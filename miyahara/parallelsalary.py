import sys, func_salary

salary = sys.argv

for i in salary[1:]:
    payamount, tax =func_salary.calcsalary(int(i))
    print("給与:{}、支給額:{}、税額:{}".format(i,payamount,tax))
