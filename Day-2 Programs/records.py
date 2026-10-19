def analyze_students(records):
    qualified=[]
    topper=""
    highest_total=0
    for student in records:
        name=student[0]
        total=student[1]+student[2]+student[3]
        average=total/3
        if average>=75:
            qualified.append(name)
        if total>highest_total:
            highest_total=total
            topper=name
    return{"qualified":qualified,"topper":topper}
records=[("Asha",85,78,92),("Bala",65,72,70),("Charan",90,88,95),("Divya",76,80,74),("Esha",60,68,72)]
print(analyze_students(records))