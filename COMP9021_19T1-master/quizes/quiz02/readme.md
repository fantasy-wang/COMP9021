# Quiz2

## 知识点讲解

### 赋值
```
    # 单行赋值
    a = b
    # 多行赋值
    a,b = c,d
```

### 字符串操作
```
    # 字符串截取
    words = 'abcdefg'
    
    # a
    print(word[0])
    # gfedcba
    print(word[::-1]
    # bc
    print(words[1:3])
    # gf
    print(words[-1:-3:-1])
    
    # 转成倒序的list
    print(list(reversed(words)))
```

### 列表生成式
```
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}
```

### 字典操作
```
    # 判断字典是否存在
    fruits = {'apple':2, 'orange':2}
    # key check
    'banana' in fruits
    'banana' not in fruits
    
    list1 = ['apple','orange']
    number = 0
    dict1 = dict.fromkeys(list1, number)
```

请注意：

在 describe_rule()方法的测试里面为了正常测试，去掉了空行。

在代码总的第42行：    # print() 提交代码的时候请注意。