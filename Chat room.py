s=input()
k="hello"
t=0
for i in s:
    if t<5 and i==k[t] :
        t+=1
    elif t==5:
        break
if t==5:
    print('YES')
else:
    print("NO")
