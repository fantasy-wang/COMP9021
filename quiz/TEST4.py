from itertools import product
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list7 = []
for i in product([0,1],repeat=5):
    list1.append(i)
for i in range(len(list1)):
    list1[i] = list(list1[i])
print(list1)
list2 = [[0, 0, 0, 0, 0],[1, 1, 1, 1, 1]]
for i in range(len(list2)):
    list1.remove(list2[i])
print(list1)
list3 = [0, 0, 0, 0, 1]
list1.append(list3)
print(list1)
if list3 in list1:
    print('true')