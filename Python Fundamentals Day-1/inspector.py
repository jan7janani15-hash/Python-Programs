x=input()
print("Original value type :",type(x).__name__)
try:
 a=int(x)
 print("Integer value :",a)
 print("Integer type :",type(a).__name__)
except:
 print("Invalid integer conversion")
try:
 b=float(x)
 print("Float value :",b)
 print("Float type :",type(b).__name__)
except:
 print("Invalid float conversion")