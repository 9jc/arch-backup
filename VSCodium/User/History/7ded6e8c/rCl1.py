def gcd_func(n1,n2):
    i=1
    while(i<=n1 and i<=n2):
        if(n1%i==0 and n2%i==0):    
            i=i+1
        return gcd

n1 = int(input("enter 1st number"))
n2 = int(input("enter 2nd number"))
gcd=gcd_func(n1, n2)
