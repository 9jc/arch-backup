def gcd_func(num1,num2):
    i=1
    while(i<=num1 and i<=num2):
        if(num1%i==0 and num2%i==0):
            gcd = i
        i=i+1
    return gcd

n1 = int(input("enter the first number :"))
n2 = int(input("enter the second number :"))
gcd = gcd_func(n1,n2)
print("GCD is",gcd)


