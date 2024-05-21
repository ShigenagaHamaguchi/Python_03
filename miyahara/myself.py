import sys
import introduce

name = sys.argv[1]
age = sys.argv[2]

myself = introduce.Intro(name, age)
print(myself.name_out())
print(myself.age_out())