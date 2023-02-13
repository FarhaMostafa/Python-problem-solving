t=int(input())
a=1
b=0
while t:
    n=int(input())
    for count,i in enumerate(range(n)):
        a+=count+(count+1)
       
    b=n-a
    print(a,"  ",b)
    t-=1



