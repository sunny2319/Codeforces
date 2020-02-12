# your code goes here
n=input()
c1=0
c2=0
c3=0
for i in n:
	if i=='1':
		c1+=1
	if i=='2':
		c2+=1
	if i=='3':
		c3+=1
if c1!=0:
	print("1",end="")
	c1-=1
elif c2!=0:
	print("2",end="")
	c2-=1
elif c3!=0:
	print("3",end="")
	c3-=1
while c1!=0:
	c1-=1
	print("+1",end="")
while c2!=0:
	c2-=1
	print("+2",end="")
while c3!=0:
	c3-=1
	print("+3",end="")
