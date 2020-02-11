# your code goes here
s=input()
st=""
for i in s:
	if i.upper() in ["A", "O", "Y", "E", "U", "I"]:
		continue
	else:
		st+="."+i.lower()
print(st)
		
