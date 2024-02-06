def elem_in_list(lst,elem):
    for i in lst:
        if i==elem:
            return True
    return False    


def onlyUnique(lst):
    uniqueLst = []
    for i in lst:
        if not(elem_in_list(uniqueLst,i)):
            uniqueLst.append(i)
    return uniqueLst

lst = [1,1,2,2,3,3,3,8,8,8]
print(onlyUnique(lst))