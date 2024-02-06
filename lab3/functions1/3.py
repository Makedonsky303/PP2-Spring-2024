from math import ceil

def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chickens = numheads - rabbits

    if rabbits != ceil(rabbits) or (numlegs - 2*numheads)/2<0: 
        return "Error"
    else:
        return [rabbits,chickens]

    
    
print(solve(35,94))