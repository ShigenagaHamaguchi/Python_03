
from introduce import Intro
import sys
# オブジェクト＝データとそのデータを操作するための関数を持ったもの
myself = Intro(name=sys.argv[1],age=sys.argv[2])
print(myself.name_out())
print(myself.age_out())
# fujii = Intro(name="Fujii",age=22)

