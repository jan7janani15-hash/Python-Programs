import numpy as np
def detect_outliers(values):
    a=np.array(values)
    mean=np.mean(a)
    std=np.std(a)
    z=abs((a-mean)/std)
    return [float(x) for x in a[z>2]]
numbers=[10,12,12,13,12,11,14,100,12]
print(detect_outliers(numbers))