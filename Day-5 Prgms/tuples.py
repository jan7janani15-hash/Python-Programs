products=[("Sensor",4,150.0),("Cable",12,25.0),("Board",3,800.0)]
low=[]
total=0
for p in products:
    value=p[1]*p[2]
    print(f"{p[0]}:Value={value:.2f}")
    total+=value
    if p[1]<5:
        low.append(p[0])
print("Low-stock products:",low)
print(f"Total inventory value:{total:.2f}")