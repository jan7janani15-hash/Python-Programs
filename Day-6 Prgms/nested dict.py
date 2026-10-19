records=[('D01','Lab-A','READY'),('D02','Lab-B','BUSY'),('D01','Lab-C','MAINTENANCE')]
result={}
for id,location,status in records:
    result[id]={'location':location,'status':status}
print(result)