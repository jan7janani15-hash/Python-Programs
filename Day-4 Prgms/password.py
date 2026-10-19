s=input()
u=l=d=sp=False
for i in s:
    if i.isupper():
        u=True
    elif i.islower():
        l=True
    elif i.isdigit():
        d=True
    else:
        sp=True
if len(s)>=8 and u and l and d and sp:
    print("Valid password")
else:
    print("Invalid password")
print("Uppercase:","Present" if u else "Missing")
print("Lowercase:","Present" if l else "Missing")
print("Digit:","Present" if d else "Missing")
print("Special character:","Present" if sp else "Missing")
print("Minimum length:","Satisfied" if len(s)>=8 else "Not satisfied")