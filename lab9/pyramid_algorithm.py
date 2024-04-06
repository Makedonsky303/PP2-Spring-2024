a = 9
b = 3

for k in range(1,a+1):
    for l in range(1,b+1):
        if (a-(l-1)*b - (a+1) + k) >=0:
            print("(",k,",",l,")", end=" ")
    print()
  