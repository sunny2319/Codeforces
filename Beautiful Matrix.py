# your code goes here
arr=[]
for i in range(5):
	x=list(map(int,input().split()))
	arr.append(x)
x=0
y=0
f=0
for i in range(5):
	for j in range(5):
		if arr[i][j]==1:
			x=i
			y=j
			f=1
			break
	if f==1:
		break
z=abs(x-2)+abs(y-2)
print(z)
