def si(p,n,r):
    return p*n*r / 100
p,n,r=input("enter the principle,no of year,rate of interest>").split()
print(si(int(p),int(n),int(r)))
