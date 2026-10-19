try:
    a = int(input("Integer: "))
    b = float(input("Decimal: "))
    print("Integer Value :", a)
    print("Integer Type  :", type(a).__name__)
    print("Float Value   :", b)
    print("Float Type    :", type(b).__name__)
    print("Rounded Value :", round(b))
    print(a, "/", 12, "=", round(a/12, 4))
    print(a, "//", 12, "=", a//12)
    print(a, "%", 12, "=", a%12)
    print(a, "**", 2, "=", a**2)
except:
    print("Invalid input")