def isPrime(num):
    if num<2:
        return False
    
    for i in range(2,int(num**0.5 + 1)):
        if(num%i==0):
            return False
    return True

def filter_prime(lst):
    newLst = []
    for i in lst:
        if isPrime(i):
            newLst.append(i)

    return newLst

myLst = [1,5,6,7,13,21,48,31]
print(filter_prime(myLst))