import re

txt = "a some_text b"

x = re.search('^a.*b$',txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")