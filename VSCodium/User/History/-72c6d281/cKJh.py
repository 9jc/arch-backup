n=int(input("enter the input of n:"))
term=int(input("enter the no. of iterations: "))
pprox=0.5*n
for i in range(term):
    better_res=0.5*(approx+n/approx)
    approx=better_res
print("the square root of given number",n,"is=",approx)
