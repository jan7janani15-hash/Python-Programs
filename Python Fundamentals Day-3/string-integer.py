s=input().strip()
i=0
sign=1
if s and s[0]=='-':
    sign=-1
    i=1
elif s and s[0]=='+':
    i=1
n=0
while i<len(s) and s[i].isdigit():
    n=n*10+int(s[i])
    i+=1
print(sign*n)