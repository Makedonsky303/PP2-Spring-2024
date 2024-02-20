import re 

txt = "Python Is A Great Programming Language"

lst = re.findall(r'[A-Z][a-z]*|[a-z]+',txt)

print(lst)