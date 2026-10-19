readings=[8,10,20,35,51,40]
a=[round(i*9/5+32,1) 
   for i in readings 
   if 10<=i<=50]
print("Converted readings:",a)