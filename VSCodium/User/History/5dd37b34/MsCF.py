def first_prime_number():
    flag=False
    count=0
    i=3
    n=int(input("Enter the number of terms :"))
    while(count<n):
        for j in range(2,i):
            if(i%j==0):
                flag=True
        if(flag==False):
            print(i)
            count=count+1
        i=i+1
        flag=False

first_prime_number()

