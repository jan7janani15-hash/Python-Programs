import re
def extract_contacts(text):
    emails=[]
    phones=[]
    words=text.split()
    for x in words:
        if "@" in x:
            emails.append(x)
        elif x.isdigit() and len(x)==10:
            phones.append(x)
    return{"emails":emails,
           "phones":phones}
text="ravi.kumar@techcorp.in, +91 9876543210"
print(extract_contacts(text))