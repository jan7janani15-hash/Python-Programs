def parse_numeric_log(logs)
    valid=[]
    s=0
    for x in logs
        try
            a,b=x.split(,)
            valid.append({ida.strip(), valuefloat(b)})
        except
            s+= 1
    return{validvalid,
           corrupted_counts}
logs=[TXN101, 145.50,TXN102, invalid_num,TXN103, 300.00,CORRUPTED_LINE,TXN104, 82.25]
print(parse_numeric_log(logs))