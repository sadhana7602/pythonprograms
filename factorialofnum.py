def fact(a):
    while(a>0):
        if(a==0 or a==1):
            return 1
        else:
            return a*fact(a-1)
c=int(input("enter the number>"))
print(fact(c))
