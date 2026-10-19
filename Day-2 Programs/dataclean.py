data=[
    "Asha,Chennai,25 ","Bala,Chennai,30","Asha,Chennai,25","Charan,Bangalore,28","Bala,Chennai,30 "]
result=[]
seen=set()
for record in data:
    parts=record.strip().split(",")
    name=parts[0].strip().title()
    city=parts[1].strip().title()
    age=int(parts[2].strip())
    key=(name.lower(), city.lower(), age)
    if key not in seen:
        seen.add(key)
        result.append({"Name":name,"City":city,"Age":age})
print(result)