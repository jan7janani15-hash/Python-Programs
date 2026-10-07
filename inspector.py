text=input("Enter a value:")
print("Original value type:",type(text).__name__)
try:
    i=int(text)
    print("Integer value:",i)
    print("Integer type:",type(i).__name__)
except ValueError:
    print("Invalid integer conversion")
try:
    fl=float(text)
    print("Float value:",fl)
    print("Float type:",type(fl).__name__)
except ValueError:
    print("Invalid float conversion")