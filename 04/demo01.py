#变量实验
# type 功能用来 查看数据类型
var01 = 7
print(var01)
print(type(var01))

var02 = 7.0
print(var02)
print(type(var02))

var03 =  '7'
print(var03)
print(type(var03))

print(var01+var01) #运算
print(var03+var03) #拼接
print(var01+var02) #运算
#无法运算:print(var01+var03)

print(var01*4)
print(var03*4)
print('*'*100)
print('+'*100)
print(7+int('7'))
print(str(7)+'7')

#有这样的情况 int 只能转换数字类字符串
#如果放置变量的时候 字符串很长 则需要特殊处理
var04 = 'nsnfownaofwmlasdml;a'
print(var04)
print('*'*300)

var05 = '''nsdkjawktmfj934ui2j9 
kj2o3jk,dalms /.;sd.,;.a
klajrk4e.,asdkwo,.
'''
print(var05)

#计算字符串的长度 len()
print(len(var05))

# 如果出现特殊字符串 需要特殊处理 \n代表回车 则需在需在字符串最前面加上r，关闭特殊转换
var06='c:\now'
print(var06)

var07=r'c:\now'
print(var07)