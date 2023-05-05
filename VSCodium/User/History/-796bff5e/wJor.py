li=[ ]
n=int(input("Enter number of elements in list"))
for i in range(0,n):
    inp=int(input("Enter the number"))
    li.append(inp)

print(" The elements in the list:",li)

max_val=li[0]
for i in li:
if(i>max_val):
    max_val=i

print("Maximum of the list is:",max_val)