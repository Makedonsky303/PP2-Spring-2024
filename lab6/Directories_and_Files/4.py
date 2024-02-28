counter = 0

f = open("example.txt","w") 
for i in range(1,10+1):
        f.write(str(i)+"\n")
f.close()        

f = open("example.txt","r")
for i in f:
    counter+=1
    
print(counter)            