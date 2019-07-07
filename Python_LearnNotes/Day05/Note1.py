"""
python中使用 \n 来添加新行,使用 反斜线（\）来换行

Python 的元组与列表类似，不同之处在于元组的元素不能修改，但我们可以对元组进行连接组合。
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3)
元组使用小括号，列表使用方括号。元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

tuple(seq) 将列表转换为元组。

把相应的键放入熟悉的方括弧，如下实例:
dict = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。

显示删除一个字典用del命令，如下实例：
dict = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键 'Name'
dict.clear()     # 删除字典
del dict         # 删除字典


迭代器与生成器：

迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器：
迭代器对象可以使用常规for语句进行遍历：

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")



也可以使用 next() 函数：
import sys         # 引入 sys 模块

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象

while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()


生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
以下实例使用 yield 实现斐波那契数列：

import sys

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()






"""