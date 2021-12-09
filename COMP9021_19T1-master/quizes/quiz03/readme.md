# Q3 知识点讲解

## 列表操作

### 列表的遍历
```
    for index in range(len(L)):
        index,L[index]
        
    index = 0
    for item in L:
        index, item
        
    for index, item in enumerate(L)
        index, item
        
    index = 0
    while index < len(L):
        index, L[index]
    
```

### 列表合并
```
    from itertools import chains
    from itertools import zip_longest
    
    list2 = chains(list1,list1)
    list2 = zip_longest(list1,list2)
    
```

### 列表的遍历2
```
    for index in range(len(L) - 1 ):
        first,second = L[index], L[index + 1]
    
    first = L[0]
    for second in L[1:]:
        print(first,second)
        first = second
        
        {index:value for index,value in enumerate(L)}
```

### 字典的列表生成式
```
    dictionary = {index:value for index,value in enumerate(L)}
    
    dictionary = {}
    for index,value in enumerate(L):
        dictionary[index] = value
```

### 比较大小
```
    max_length,length
    
    if max_length > length:
        max_length = length
        
    max_length = max(max_length,length)
    
    max(L)
    min(L)
    avg(L)
```