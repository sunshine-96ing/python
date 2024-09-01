#认识常见的数字
print(1+1)
print("5*2")
print(5*2)

#认识常用的数据操作符号+ - * /
print(10/2)
print(10//2)
print(11/2)
print(11//2)

#除法的余数部分 使用%
print(11%2)

# 数学的运算优先级 * / 优于+ -
print(5+5*3)
print((5+5)*3) # 使用 括号可以修改优先级

#各种进位数的使用转换
x=60
print(x)
print(bin(x)) # 转换成2进制
print(hex(x)) # 转换成16进制
print(oct(x)) # 转换成8进制

#作业练习：计算 sin（π/4）+lg5e
import math
print(math.pi)
print(math.sin(math.pi/4))
print(math.log10(10000))
print(1e5) #科学计数法
print(2e4)
x = math.log10(5 * math.e)
print(x)
print('{:.2F}'.format(math.pi))
print('{:.2F}'.format(math.sin(math.pi/4)+math.log10(5 * math.e)))