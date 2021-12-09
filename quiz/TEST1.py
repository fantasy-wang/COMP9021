list1 = '-2x^7 + 5x^6 - 9x^5 + 14x^4 - 12x^3 + 9x^2 - 5x'.split(' ')
print(list1)
list2=[]
list3=[]
list4=[]
list5=[]
dict1={}
if len(list1)>=1:
    if list1[0].isdigit():
        list4.append(list1[0])
    else:
        for i in range(len(list1[0])):
            if list1[0][i] is '-':
                list2.append(-1)
            if list1[0][i] is '+':
                list2.append(1)
            if list1[0][i] is 'x':
                if i <len(list1[0])-1:
                    if list1[0][i+1] is '^':
                        list3.append(list1[0][i+2])
                if i==len(list1[0])-1:
                    list3.append(1)
if len(list1)>=2:
    for i in range(1,len(list1)):
        if list1[i] is '-':
            list2.append(-1)
        if list1[i] is '+':
            list2.append(1)
        if 'x' in list1[i]:
            for j in range(len(list1[i])):
                if list1[i][j] is 'x':
                    list4.append(list1[i][:j])
                    if j < len(list1[i]) - 1:
                        if list1[i][j + 1] is '^':
                            list3.append(list1[i][j + 2])
                    if j == len(list1[i]) - 1:
                        list3.append(1)
        if list1[i].isdigit():
            list4.append(list1[i])
for i in range(len(list3)):
    list3[i]=int(list3[i])
for i in range(len(list4)):
    list4[i]=int(list4[i])
for i in range(len(list2)):
    a1=list2[i]*list4[i]
    list5.append(a1)
for i in range(len(list3)):
    dict1[list3[i]]=list5[i]
