#1
# def squares(n):
#     for i in range(1,n+1):
#         yield i**2
# x = int(input())        

# for i in squares(x):
#     print(i)

#2
# def even(n):
#     for i in range(n+1):
#         if i%2==0:
#             yield i 

# x = int(input())        

# for i in even(x):
#     print(i,end=",") 

#3
# def divisible(n):
#     for i in range(n+1):
#         if i%12==0:
#             yield i 

# x = int(input())        

# for i in divisible(x):
#     print(i,end=",") 

#4
# def squares(a,b):
#     for i in range(a,b+1):    
#         yield i**2 

# a = int(input())        
# b = int(input())        

# for i in squares(a,b):
#     print(i) 

#5
def seq(n):
    
    while n>=0:   
        yield n
        n-=1

x = int(input())        
        

for i in seq(x):
    print(i) 

              
                            