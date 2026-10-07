a=int(input("Withdrawal Amount: "))
if a>20000 or a%10!=0:
    print("Transaction Rejected")
else:
    n500=a//500
    a%=500
    n200=a//200
    a%=20
    n100=a//100
    a%=100
    n50=a//50
    a%=50
    n10=a//10
    print("₹500 notes :",n500)
    print("₹200 notes :",n200)
    print("₹100 notes :",n100)
    print("₹50 notes :",n50)
    print("₹10 notes :",n10)