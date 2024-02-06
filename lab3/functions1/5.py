from itertools import permutations

def allPermutations(s):
    lst = sorted(list(s))
    
    perm = permutations(lst)

    for i in list(perm):
        print(i)

allPermutations("john")