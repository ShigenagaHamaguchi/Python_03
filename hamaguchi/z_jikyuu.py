# 時給の入力
user = input("時給はいくらですか?: ")
jikyuu  = int(user)
# 働いた時間の入力
user = input("何時間はたらきましたか?: ")
jikan = int(user)

# 給料の計算
salary = jikan*jikyuu

# アウトプット文を出力
fmt = '''時給{0}円で、{1}じかん働いたので、
給料は、{2}円です。 '''.format(jikyuu,jikan,salary)

print(fmt)