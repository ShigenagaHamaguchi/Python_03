import sys
args = sys.argv

#引数を変数に代入
food = args[1]

#引数foodの中身を""で囲んで表示する
print("I don't like", "\"" + food + "\"", end="")