import numpy as np
import math

def floatBin(decVal):
    decVal = str(decVal)
    pnt = decVal.index('.')
    decVal.pop('.')
    

i=0
e=np.float32(1.0)
while (np.float32(1+e/2)>1):
    e=np.float32(e/2)
    i=i+1
print("Machine epsilon float32 = ", e, "\nbinary degree = -", i)
e32 = e

i=0
e=np.float64(1.0)
while (np.float64(1+e/2)>1):
    e=np.float64(e/2)
    i=i+1
print("Machine epsilon float64 = ", e, "\nbinary degree = -", i)
e64 = e

if 1+e+e/2>1+e:
    print("1+e+e/2 more than 1+e")
else:
    print("equal")

print("1+e = ",1+e,"\n1+e/2 = ",1+e/2,"\n1+e+e/2 = ",1+e+e/2, "\n1+e/2+e = ", 1+e/2+e)

print("numpy float32:")
i=0
m = np.float32(1.0)
while np.float32(m*2)<np.float32('inf'):
	i = i + 1
	m = np.float32(m * 2)
print(np.float32(m * (2-2*e32)), i)
i = 0
m = np.float32(1.0)
while np.float32(m/2)>0:
	i = i + 1
	m = np.float32(m/2)
print(m, -i)

print("numpy float64:")
i=0
m = np.float64(1.0)
while m*2<np.float64('inf'):
	i = i + 1
	m = np.float64(m * 2)
print(np.float64(m * (2-2*e64)), i)
i = 0
m = np.float64(1.0)
while np.float64(m/2)>0:
	i = i + 1
	m = np.float64(m/2)
print(m, -i)
#because mantissa of e, e/2 is 0 and different degree
#but mantissa of e+e/2 is 10000... more than 0000... with same degree
