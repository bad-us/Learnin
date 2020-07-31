len_list = int(input("enter the number of values in the list "))
list1 = []
i = 0
el = 0
while i < len_list:
    i += 1
    list1.append(input("Enter value "))
print(list1)
for elem in range(int(len(list1) / 2)):
    list1[el], list1[el + 1] = list1[el + 1], list1[el]
    el += 2
    print(list1)
