# cook your dish here
n=int(input())
k=list(map(int,input().split()))
k.sort()
s=sum(k)
t1=0
t2=s
i=0
while i<n:
    if (t1+k[i]) < (t2-k[i]):
        t1+=k[i]
        t2-=k[i]
    else:
        break
    i+=1
print(n-i)
    

