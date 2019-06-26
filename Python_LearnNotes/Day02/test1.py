# coding=utf-8
# 华氏温度转换成摄氏温度
"""
华氏温度和摄氏温度的相互转换
1C = (F- 32)* 5/9
1F = C*9/5 + 32
C是摄氏温度,F是华氏温度

"""

# 输入
f = float(input('输入华氏温度: '))
# 计算华氏温度
c = (f - 32) * 5 / 9
print('%0.1f 华氏温度转为摄氏温度为 %0.1f ' % (f, c))

