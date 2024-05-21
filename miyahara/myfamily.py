import sys
from introfamily import IntroFam

name = sys.argv[1]
age = sys.argv[2]
cat = sys.argv[3]


myfamily = IntroFam(name, age, cat)

print(myfamily.name_out())
print(myfamily.age_out())
print(myfamily.cat_out())