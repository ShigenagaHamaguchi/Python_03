import sys

"""
CLIの引数から嫌いな食べ物を取得し、嫌いな食べ物を出力
"""
for food in sys.argv[1:]:
    print("I don't like "+'"'+food+'"',end="")