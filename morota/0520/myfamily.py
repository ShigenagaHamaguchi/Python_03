from introduce import Intro
from introfamily import IntroFam

import sys
args = sys.argv

intro_txt = Intro(args[1], args[2])
introfam_txt = IntroFam(args[3])

print(intro_txt.name_out())
print(intro_txt.age_out())
print(introfam_txt.cat_out())