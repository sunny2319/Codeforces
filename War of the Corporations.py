# your code goes here
s1=input()
s2=input()
n1=len(s1)
n2=len(s2)
c=0
i=0
while i<=n1-n2+1:
	st=s1[i:i+n2]
	if st==s2:
		c+=1
		i=i+n2
	else:
		i+=1
print(c)
