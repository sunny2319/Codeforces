# your code goes here
i1=input().lower()
i2=input().lower()
max=0
for i in range(len(i1)):
	if i1[i]==i2[i]:
		max=0
	elif i1[i]<i2[i]:
		max=-1
		break
	else:
		max=1
		break
print(max)
