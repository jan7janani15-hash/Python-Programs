s='ADOBECODEBANC'
t='ABC'
result=''
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        if all(sub.count(c)>=t.count(c) for c in t):
            if result=='' or len(sub)<len(result):
                result=sub
            break
print("Minimum window:",repr(result))