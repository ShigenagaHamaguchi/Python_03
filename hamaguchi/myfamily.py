from introfamily import IntroInfo

import sys


myfamily = IntroInfo(name=sys.argv[1],age=sys.argv[2],cat=sys.argv[3])

print(myfamily.name_out())
print(myfamily.age_out())
print(myfamily.cat_out())
