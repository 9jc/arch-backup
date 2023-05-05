ele=[]
terms=int(input("Enter the number of elements"))
for i in range(0,terms):
    ele.append(int(input("Enter the element")))
print("Elements before selection sort",ele)

for ind in range(0,terms):
    min_index = ind
    for j in range(ind + 1, terms):
       	if ele[j] < ele[min_index]:
           	min_index = j
    (ele[ind], ele[min_index]) = (ele[min_index], ele[ind])
print("Elements after selection sort",ele)
