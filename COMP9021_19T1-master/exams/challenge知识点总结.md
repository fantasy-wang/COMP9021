# 期末考试总结：
## 考试注意事项
* 必须先讲所有的题过一遍，有的题难，有的题简单，选择简单的题型入手
* 如果一个题5分钟以内没有思路，立即跳过
* 审题
* 用自己最擅长的思路写代码
* 每个题完成就提交
* 留出时间检查

## 如果debug自己的代码
* 快捷键
* 帮助函数

## Labs
### Lab1 计算温度
```
    格式化输出：
    左对齐，右对齐
    
    
    
    # for 直接遍历 可以遍历的对象
    for x in set/list/string/map
    for x in range(2,100,2)
    
    
    for num in range(10,20):  # 迭代 10 到 20 之间的数字
        for i in range(2,num): # 根据因子迭代
        if num%i == 0:      # 确定第一个因子
            j=num/i          # 计算第二个因子
            print '%d 等于 %d * %d' % (num,i,j)
            break            # 跳出当前循环
        else:                  # 循环的 else 部分
            print num, '是一个质数'
```
### Lab2 Min Max 相关计算
https://docs.python.org/3/library/functions.html
```
    max
    min
    avg
    abs
    len
    all
    any
    zip
    round
    char
    bin
    set
    sorted
    divmod
    eval
    sum
    ascii
```
### lab3 dict的简单应用
```
    dict = {}
    dict = {x:0 for x in 'abcd'}
    dict[x] = 1
    dict.get(x,0)
    defaultdict
```
### dict的高级应用
```
    defaultdict
    Counter
    for k,v in dict.iterms()
    keys = dict.keys()
    values = dict.values()
    sorted(keys)
    sorted(dict.items(),key = lambda item:item[0])
    sorted(dict.items(),key = lambda item:item[1])
```
### Lab4 均值，中位数，方差
```
    from math import sqrt
    from statistics import mean, median, pstdev
    5 ** 5
```
### Lab5 数0的个数
```
    from math import factorial
    
    两种方式
    一种是string
    一种是while
    
    可以用reversed的方式计算
    // %
    divmod
```

### Lab6 列表相关操作
```
    sum()
    all
    any
```



### Lab13
```
prime_factors = {}
    p = 2
    while n != 1:
        if n % p == 0:
            k = 1
            while n % p == 0:
                n //= p
                k += 1
            # prime_factors[p] is 1 + p's multiplicity in n
            prime_factors[p] = k
        p += 1
```

## 代码总结
### 求素数
### 除法算子
```
    计算因子之和
    计算所有的因子
    计算唯一的因子
    any
```

