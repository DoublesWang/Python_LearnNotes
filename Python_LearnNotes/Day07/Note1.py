"""
要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
>>> f = open('/Users/michael/test.txt', 'r')
标示符'r'表示读，这样，我们就成功地打开了一个文件。
如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在;
如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示;
最后一步是调用close()方法关闭文件。

由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open('/path/to/file', 'r') as f:
    print(f.read())
这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
这也是日常最常用的用法。


二进制文件
前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()

字符编码
要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()

写文件
写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。


异常：
即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
大多数的异常都不会被程序处理，都以错误信息的形式展现

异常处理
以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。用户中断的信息会引发一个 KeyboardInterrupt 异常。

>>>while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")
try语句按照如下方式工作；

首先，执行try子句（在关键字try和关键字except之间的语句）
如果没有异常发生，忽略except子句，try子句执行后结束。
如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。

处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。


try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。例如:

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到的、而except又没有捕获的异常。

抛出异常：Python 使用 raise 语句抛出一个指定的异常。
例如:

>>>raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: HiThere
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。

用户自定义异常
你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，例如:

>>>class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
>>> try:
        raise MyError(2*2)
    except MyError as e:
        print('My exception occurred, value:', e.value)

My exception occurred, value: 4
>>> raise MyError('oops!')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
__main__.MyError: 'oops!'

在这个例子中，类 Exception 默认的 __init__() 被覆盖。


数据持久化:
1.python操作csv文件：

    #读操作
    import csv
    with open("/路径/文件名.csv","r") as csvfile: #固定写法，使用open()方法，可以避免还要关闭file，'r'表示读操作
        read=csv.reader(csvfile)    #使用csv.reader()方法，读取打开的文件，返回为可迭代类型
        for i in read:
            print i

    #写操作
    import csv
    with open("/路径/文件名.csv","w") as csvfile: #'w'表示写操作，有则修改,无则新建
        write=csv.writer(csvfile)
        write.writerow(data)    #写入一行操作，data为可迭代类型，如果为字符串，则单个字符为一个元素
        write.writerows(data)   #写入多行操作，data中一个元素为一行

2、json数据格式：
JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式，JSON 是存储和交换文本信息的语法，类似xml。

JSON 的语法基本上可以视为 JavaScript 语法的一个子集，包括以下内容：

数据使用名/值对表示。
使用大括号保存对象，每个名称后面跟着一个 ':'（冒号），名/值对使用 ,（逗号）分割。
使用方括号保存数组，数组值使用 ,（逗号）分割。
下面是一个简单的示例：

{
    "book": [
        {
            "id":"01",
            "language": "Java",
            "edition": "third",
            "author": "Herbert Schildt"
        },
        {
            "id":"07",
            "language": "C++",
            "edition": "second"
            "author": "E.Balagurusamy"
    }]
}

JSON 语法规则
JSON 语法是 JavaScript 对象表示法语法的子集。

JSON 语法规则不复杂，它参考了 C 语言家族的一些习惯，学习起来并不会感到陌生。
数据在名称/值对中
数据由逗号分隔
花括号保存对象
方括号保存数组

JSON 对象
JSON 对象在花括号（{}）中书写：

对象可以包含多个名称/值对：  { "firstName":"John" , "lastName":"Doe" }


JSON 数组
JSON 数组在方括号中书写：

数组可包含多个对象：

{
"employees": [
{ "firstName":"John" , "lastName":"Doe" },
{ "firstName":"Anna" , "lastName":"Smith" },
{ "firstName":"Peter" , "lastName":"Jones" }
]
}

"""