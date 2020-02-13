n=int(input())
k=list(map(int,input().split()))
m1=-2**31
mi=0
mini=2**31-1
minind=0
for i in range(n):
	if k[i]>m1:
		m1=k[i]
		mi=i
	if k[i]<=mini:
		mini=k[i]
		minind=i
if minind<mi:
	x=mi+n-minind-2
	print(x)
else:
	x=mi+n-minind-1
	print(x)
