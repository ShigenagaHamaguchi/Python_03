"""
入力された数字に対して素因数分解するプログラム
"""

import sys

x = int(sys.argv[1])
prime_nums = []

"""
素因数分解を行う。
対象の値xに対して、任意の素数が割り切れるか判定する。
割り切れる限り対象の値を割り、割った解を対象の値xとする。
対象の値xが割り続ける限り、対象の値を更新し続けるプログラム。

"""
for i in range(2,x//2+2):
    if x % i != 0:continue
    while x % i == 0:
        prime_nums.append(i) #割り切れた場合prime_numsに登録する。
        x = x // i

print(prime_nums,end="")