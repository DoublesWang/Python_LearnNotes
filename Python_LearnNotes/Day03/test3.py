# coding=utf-8

# Fibonacci数列为：0、1、1、2、3、5、8、13、21......


def fibo(n):
    if n < 3:
        return 1
    return fibo(n - 1) + fibo(n - 2)


for i in range(10):
    print(fibo(i))