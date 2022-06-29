list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
# checking each number in the list

lis = []
for numm in list2:
    if numm >= 0:
        lis.append(numm)
print(f'output for list2: {lis}')

for num in list1:
    if num >= 0:
        print(num, end=" ")
