from itertools import product

sum1 = 0
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
for k in product([0, 1], repeat=11):
    list7.append(k)
for i in range(len(list7)):
    list7[i] = list(list7[i])
list8 = list7[:]
for i in range(len(list7)):
    for j in range(len(list7[i])):
        if list7[i][0] == 1:
            for k in range(len(list7[i])):
                if k != 0:
                    sum1 += list7[i][k]
                if sum1 != len(list7[i])-1:
                    list9.append(list7[i])
        if list7[i][0] == 0:
            for k in range(len(list7[i])):
                if k != 0:
                    sum1 += list7[i][k]
                if sum1 == len(list7[i])-1:
                    list10.append(list7[i])
for k in range(len(list9)):
    if list9[k] in list7:
        list7.remove(list9[k])
for k in range(len(list10)):
    if list10[k] in list7:
        list7.remove(list10[k])
print(len(list7))