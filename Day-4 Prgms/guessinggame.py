s=8
for i in range(5):
    n=int(input())
    if n<s:
        print("Too Low")
    elif n>s:
        print("Too High")
    else:
        print("Correct")
        break
else:
    print("Game Over")