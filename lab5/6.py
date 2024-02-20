import re

txt = "a.b, c ,b.a"

x = re.sub('[ ,.]',":",txt)

print(x)