# your code goes here
n=int(input())
k=list(map(int,input().split()))
a=[0]*(n+1)
for i in range(n):
	a[k[i]]=i+1
for i in range(n):
	print(a[i+1],end=" ")
