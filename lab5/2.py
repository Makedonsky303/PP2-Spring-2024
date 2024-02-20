import re

txt = "abbbb"
x = re.search("^a(b{2}|b{3})$",txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")
