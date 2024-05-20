from introduce import Intro

import sys
args = sys.argv

text = Intro(args[1], args[2])

print(text.name_out())
print(text.age_out())

# パターン２
# import introduce
# text = introduce.Intro(args[1], args[2])