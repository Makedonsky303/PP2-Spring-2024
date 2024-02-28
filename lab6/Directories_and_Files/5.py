def list_to_str(lst):
    mystr = "["
    for i in lst:
        mystr+=i+", "
    if len(lst)>0:    
        mystr = mystr[:-2]
    mystr+="]"
    return mystr    

lst = [x for x in "QWERTY ASD"]

with open("list.txt","w") as f:
    f.write(list_to_str(lst))
    # f.writelines(lst)
