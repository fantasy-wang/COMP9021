# Written by *** and Eric Martin for COMP9021


def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}


def describe_rule(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    >>> describe_rule(3)
    The rule encoded by 3 is:  {(0, 0): 0, (0, 1): 0, (1, 0): 1, (1, 1): 1}
    After 0 followed by 0, we draw 0
    After 0 followed by 1, we draw 0
    After 1 followed by 0, we draw 1
    After 1 followed by 1, we draw 1
    >>> describe_rule(4)
    The rule encoded by 4 is:  {(0, 0): 0, (0, 1): 1, (1, 0): 0, (1, 1): 0}
    After 0 followed by 0, we draw 0
    After 0 followed by 1, we draw 1
    After 1 followed by 0, we draw 0
    After 1 followed by 1, we draw 0
    >>> describe_rule(11)
    The rule encoded by 11 is:  {(0, 0): 1, (0, 1): 0, (1, 0): 1, (1, 1): 1}
    After 0 followed by 0, we draw 1
    After 0 followed by 1, we draw 0
    After 1 followed by 0, we draw 1
    After 1 followed by 1, we draw 1
    >>> describe_rule(14)
    The rule encoded by 14 is:  {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 0}
    After 0 followed by 0, we draw 1
    After 0 followed by 1, we draw 1
    After 1 followed by 0, we draw 1
    After 1 followed by 1, we draw 0
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    # print()
    # INSERT YOUR CODE HERE TO PRINT 4 LINES
    for (first, second), last in rule.items():
        print(f"After {first} followed by {second}, we draw {last}")


def draw_line(rule_nb, first, second, length):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).


    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".
    >>> draw_line(3, 0, 0, 1)
    0
    >>> draw_line(3, 1, 0, 5)
    10101
    >>> draw_line(4, 1, 0, 9)
    100000000
    >>> draw_line(4, 0, 1, 13)
    0110000000000
    >>> draw_line(11, 1, 0, 16)
    1010101010101010
    >>> draw_line(11, 1, 1, 19)
    1111111111111111111
    >>> draw_line(14, 0, 0, 21)
    001101101101101101101
    >>> draw_line(14, 1, 0, 22)
    1011011011011011011011
    '''
    rule = rule_encoded_by(rule_nb)
    # INSERT YOUR CODE HERE TO PRINT ONE LINE
    result = []
    # check length > 1
    if length >= 1:
        result.append(first)
    # check length  > 2
    if length >= 2:
        result.append(second)
    # check length - 2
    for i in range(2, length):
        # iterate next item
        first, second = second, rule[(first, second)]
        # append next digit
        result.append(second)

    # print the result
    print("".join((str(item) for item in result)))


def uniquely_produced_by_rule(line):
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    >>> uniquely_produced_by_rule('1100110011')
    12
    >>> uniquely_produced_by_rule('01100000')
    4
    >>> uniquely_produced_by_rule('001101101')
    14
    >>> uniquely_produced_by_rule('11111111')
    -1
    >>> uniquely_produced_by_rule('00011')
    -1
    >>> uniquely_produced_by_rule('11001')
    -1
    >>> uniquely_produced_by_rule('0010001')
    -1
    >>> uniquely_produced_by_rule('0010001')
    -1
    >>> uniquely_produced_by_rule('11111111111111110')
    -1
    '''
    # REPLACE pass ABOVE WITH YOUR CODE
    rules = {}
    if len(line) >= 2:
        first, second = line[0], line[1]

    # check length-2
    for last in line[2:]:
        # exist and not equal
        if (first, second) in rules and rules[(first, second)] != last:
            # return directly
            return -1
        # next assign
        first, second, rules[(first, second)] = second, last, last

    # check result
    if len(rules) == 4:
        keys = [('0', '0'), ('0', '1'), ('1', '0'), ('1', '1')]
        result = ""
        for key in keys:
            result += rules[key]
        return int(result, 2)
    else:
        return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(uniquely_produced_by_rule('1100110011'))
