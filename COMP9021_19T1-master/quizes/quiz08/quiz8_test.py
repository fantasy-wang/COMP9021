import re
from collections import defaultdict
from copy import deepcopy


def get_str(poly):  # 通过字符串的形式，把生成的字典打印出来
    List = []
    for factor in sorted(poly, reverse=True):  # 因为从高次到低次，所以reverse,从最高次项开始打印
        coe = int(poly[factor])
        if coe == 0:
            continue  # 不打印  coe 是 系数
        else:
            if coe > 0:  # coe 是 系数，如果系数大于0
                List.append('+')
            else:
                if coe < 0:
                    List.append('-')

        if factor == 0:  # 如果次方数 为0 的情况
            List.append(str(abs(coe)))
        else:  # 如果次数不是0的情况
            if abs(coe) == 1:  # 在次数不为0 的时候 处理系数为 1 的情况
                if factor == 1:  # 并且次数也是1
                    List.append('x')
                else:  # 这里指次数 大于 1
                    List.append(f'x^{factor}')
            else:  # 系数 > 1 d的情况
                if factor == 1:  #
                    List.append(f'{abs(coe)}x')
                else:
                    List.append(f'{abs(coe)}x^{factor}')

    if not List:
        return '0'
    if List[0] == '-':  # 对多项式的处理，去掉空格
        List[1] = '-' + List[1]
    result =  ' '.join(List)
    if result.startswith("-"):
        result = "-" + result[2:]
    else:
        result = result[2:]

    return result


class Polynomial:
    def __init__(self, polynomial=None):  # polynomial 多项式
        self.dict = defaultdict(int)
        if not polynomial:  # 如果没有多项式，为空的话
            return
        WZMsymbols = re.findall(r' \+|\- ', polynomial)  # 获取符号 + -
        WZMterms = re.split(r' \+|\- ', polynomial)  # 用 + - 进行分割，得到多项式的每一部分的
        for i in range(len(WZMterms)):
            term = WZMterms[i]
            if i == 0:  # 对第一位特殊处理
                symbol = 1
            else:  # strip() 把空格去掉
                if WZMsymbols[i - 1].strip() == '+':  # 这里是错位相对照，因为多项式的第一
                    # 位对应符号号项的第0位
                    symbol = 1  # 如果是 +  那么sign = 1
                else:
                    symbol = -1  # 否则等于 -1
            if 'x^' in term:
                coe, factor = term.split('x^')  # 用 x^ 进行分割得到前后两部分
                if coe:  # coe 为前面系数
                    # factor 是几次方，也就是幂
                    self.dict[int(factor)] = symbol * int(coe)
                else:
                    self.dict[int(factor)] = symbol * int(coe)
            else:
                if 'x' in term:
                    coe, factor = term.split('x')  # 用 x^ 进行分割得到前后两部分
                    if coe:  # coe
                        # factor 是几次方，也就是幂
                        self.dict[1] = symbol * int(coe)
                    else:
                        self.dict[0] = symbol * int(coe)
                else:
                    self.dict[0] = symbol * int(term)

        print(self.dict)

    def __add__(self, other):
        temp = self.dict.copy()
        for factor, coe in other.dict.items():
            temp[factor] += coe
        return Polynomial(get_str(temp))  # 字典改成字符串，标准输出的字符串
        # 返回Polynomial的类

    def __mul__(self, other):
        temp = defaultdict(int)
        for factor, coe in other.dict.items():
            for o, c in self.dict.items():  # 次方数相加 ，系数相乘
                temp[factor + o] += coe * c
                return Polynomial(get_str(temp))

    def __str__(self):
        return get_str(self.dict)

if __name__ == '__main__':
    # import doctest

    # doctest.testmod()

    p1 = Polynomial('2x^2 - 1')
    print(p1)