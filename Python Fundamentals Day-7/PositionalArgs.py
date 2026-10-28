def average_readings(*args):
    if len(args)==0:
        return None
    return sum(args)/len(args)
a=average_readings(10,20,30,40)
if a!=None:
    print("Average:",a)
if average_readings()==None:
    print("No readings provided")