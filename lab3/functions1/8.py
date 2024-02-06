def spy_game(nums):
    zero1 = False
    zero2 = False
    seven = False
    for i in nums:
        if i==0 and not(zero1):
            zero1 = True
        elif i==0 and zero1:
            zero2 = True
        elif i==7 and zero2:
            seven = True

        if(zero1 and zero2 and seven):
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) 