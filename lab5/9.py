import re

txt = "PythonIsAGreatProgrammingLanguage"

lst = re.sub('([a-z])([A-Z])',r'\1 \2',txt)
x = re.sub('([A-Z])([A-Z])',r'\1 \2',lst)

print(x)