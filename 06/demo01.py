str1 = 'you need python'
      # 0123456789
    #             01234  选中，输入ctrl+/ 用来注释内容
print(str1[:3])
print(str1[4:8])
print(str1[9:])
print(str1[:])  #以下三种都是一样的
print(str1)
print(str1[::1])
print(str1[::2])
print(str1[::-1])

str2 = 'hello'
str3 = 'mars'
print(str2+' '+str3)

print('+'*200)  #in
print(len('hello'))
print(len(str2))
print('hel' in 'hello')

print('+'*200)  #isdigit
str5= '650'
print(str5.isdigit())
str6= '650a'
print(str6.isdigit())

print('+'*200)  #split
str7= 'you need python'
print(str7.split(' '))

print('+'*200)   #jion
list1=['you','need','python']
print(' '.join(list1))
print('+'.join(list1))

print('+'*200)   #replace
str7= 'you need python'
print(str7)
print(str7.replace(' ',','))

print('+'*200)  #format--联动
#小王买了5个苹果 单价10元 一共多少钱 50
print('小王买了5个苹果 单价10元 一共50元')
str8 =5
price=12
total=str8*price
print('小王买了{}个苹果 单价{}元 一共{}元'.format(str8,price,total))

str9=' hello '
print(str9.replace(' ',''))
print(str7.replace(' ','*'))