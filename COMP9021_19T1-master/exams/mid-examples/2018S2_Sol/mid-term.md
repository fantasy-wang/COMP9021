# 期中考试的总结
## list的相关操作
```
    list的几种遍历方式
    items = ['a','b','c']
    for index in range(len(list)):
        item = items[index】
        
    for item in items:
    
    list.append("")
    list.pop()
    
    list的反向遍历
    reversed(items)
    items[-3:]
    items[-1]
```
## int,str的相关操作
```
    除法，除数，余数
    a / b, a // b, a % b
    
    c,d = divmod(a,b)
    
    将int 变成str以后再操作
    str.replace('0','')
    count()
```

## 因子运算
```
    # 保存因子的操作
    set 去重
    # 保留所有的因子
    list 

    因子范围：sqrt(n) + 1
    
    m = n
    for i in range(2, n + 1):
        if m == 1: break
        while m % i == 0:
            factors[i] += 1
            m = m // i
            
    for i in range(2, int(sqrt(n)) + 1):
       if n % i == 0:
           result.add(i)
           result.add(n // i)
```
## 求Prime数
```
def is_prime(n):
    # Only used to test odd numbers.
    return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))


def get_primes(n):
    if n == 1:
        return []
    if n == 2:
        return [2]

    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i ** 2 // 2::i] = bytearray((n - i ** 2 - 1) // (2 * i) + 1)
    return [2, *compress(range(3, n, 2), sieve[1:])]
```
## 文件读取
```
    csv.DictReader()
    with open("") as file:
        file.readlines()
        
```
## 列表操作
```
    # numpy 操作
    # check duplications
    
```
## 打印输出
```
    1。左侧输出
    2。边打印边输出。
    3。统一输出
```