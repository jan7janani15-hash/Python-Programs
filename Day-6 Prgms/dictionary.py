stock={'LED':20,'RESISTOR':50,'SENSOR':4}
requested=['LED','SENSOR','SWITCH']
for i in requested:
    if i in stock:
        print(i+":",stock[i],"available")
    else:
        print(i+": unavailable")