# coding=utf-8
# 输入圆的半径计算周长和面积

# 问题分析：计算圆的周长和面积需要使用π的值，Python的math模块中包含常量pi，通过导入math模块可以直接使用该值，然后使用周长和面积公式计算即可。代码如下：
import math
r = float(input('请输入圆的半径: '))
# 周长
c = 2*math.pi*r
# 面积
s = math.pi*r*r
print ( "圆的周长是: %.2f" % c)
print ( "圆的面积是: %.2f"% s)
