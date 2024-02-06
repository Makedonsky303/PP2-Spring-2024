def myReverse(s):
    s.strip()
    lst = s.split(" ")
    lst.reverse()
    newStr = " ".join(lst)
    return newStr

print(myReverse("We are ready"))