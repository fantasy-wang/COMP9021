from itertools import product
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list7 = []
for i in product([0,1],repeat=5):
    list1.append(i)
print(list1)
list4 = list1[:]
list6 = list1[:]
for i in range(1,len(list1)//2,1):
    list2.append(list1[i])
list1 = list(set(list1)-set(list2))
print(list1)
list1.sort()
print(list1)
list3 = [(0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1)]
list1 = list(set(list1)-set(list3))
list1.sort()
print(list1)
print(list4)
for i in range(len(list4)):
    print(list4[i])
    if list4[i] != (0, 0, 0, 0):
        list5.append(list4[i])
list4 = list(set(list4)-set(list5))
print(list4)
list5 = [(0, 0, 0)]
s1 = ' '
for i in list5:
    for j in range(len(i)):
        list7 = list(i)
print(list5)
print(list7)
