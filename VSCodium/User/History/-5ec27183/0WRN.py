def gcd_func(num1, num2):
  i = 1
  while (num1 <= i and num2 <= i):
    if (num1 % i == 0 and num2 % i == 0):
      gcd = i
      i = i + 1
    return gcd


num1 = int(input("enter the 1st number :"))
num2 = int(input(" enter the 2nd number :"))
gcd1 = gcd_func(num1, num2)
print("GCD IS", gcd1)
