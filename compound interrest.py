import math
def ci(p,n,r):
    return p*((pow((1+r/100),n)) -1)
p,n,r=input("enter the principle,no of year,rate of interest>").split()
print(ci(float(p),float(n),float(r)))
