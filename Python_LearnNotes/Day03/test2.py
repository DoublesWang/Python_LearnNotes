# coding=utf-8

"""
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外
的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的因子之和，则称该数为“完全数”。
"""


for i in range(1,10000):
    sum = 0
    for j in range(2,i):
        if i%j == 0:
            sum += j
        else:
            continue
    else:
        if sum+1 == i:
            print(i)





