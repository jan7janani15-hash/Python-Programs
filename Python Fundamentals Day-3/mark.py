n=int(input("Students:"))
for i in range(n):
    name=input("Name:")
    m = input().split()
    try:
        m = [int(x) for x in m]
        if max(m)>100 or min(m)<0:
            print(name,"Invalid marks")
        else:
            total=sum(m)
            avg=total/len(m)
            if avg>=80:
                grade="A"
            elif avg>=60:
                grade="B"
            else:
                grade="C"
            print(name, total,"%.2f"%avg,grade)
    except:
        print(name,"Invalid marks")