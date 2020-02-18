# your code goes here
n,t=input().split()
s=input()
n=int(n)
t=int(t)
for i in range(t):
	st=""
	j=0
	while j<n:
		if j+1<n and s[j]=='B' and s[j+1]=='G':
			st+='G'
			st+='B'
			j+=2
		else:
			st+=s[j]
			j+=1
	s=st
print(s)
		
