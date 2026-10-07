s=input("String: ")
r=""
for i in range(len(s)-1,-1,-1):
    r+=s[i]
print("Loop Reverse:",r)
print("Slice Reverse:",s[::-1])
x=s.replace(" ","").lower()
print("Palindrome:",x==x[::-1])
v=c=d=0
for i in s:
    if i.lower() in "aeiou":
        v+=1
    elif i.isalpha():
        c+=1
    elif i.isdigit():
        d+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)