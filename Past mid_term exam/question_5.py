'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    list1=[]
    list2=[]
    list3=[]
    list4= []
    str1 = ''
    with open('cpiai.csv') as c:
        for line in c:
            if '\n' in line:
                list1.append(line[:-1].split(','))
            else:
                list1.append(line)
    for i in range(len(list1)):
        if str(year) in list1[i][0]:
            list2.append(list1[i][2])
    a2 = max(list2)
    a1 = str(a2)
    for i in range(len(list1)):
        if str(year) in list1[i][0] and a1 == list1[i][2]:
            list3.append(list1[i][0][5:7])
    for i in range(len(list3)):
        list4.append(months[int(list3[i])-1])
    str1 = ', '.join(list4)
    print(f'In {year}, maximum inflation was: {a1}\nIt was achieved in the following months: {str1}')
    # Insert your code herel


if __name__ == '__main__':
    import doctest
    doctest.testmod()
