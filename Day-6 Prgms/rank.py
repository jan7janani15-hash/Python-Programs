sales={'Sensor':[4,6,5],'Cable':[10,2,3],'Board':[8,7],'LED':[5,5,5]}
for i in sorted(sales):
    print(i+':',sum(sales[i]))