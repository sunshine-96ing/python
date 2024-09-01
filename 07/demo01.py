#创建一个列表
nums = [25,12,36,95,14]
print(nums)
print(type(nums))

# 通过索引号来访问对象
print(nums[0])

#IndexError: list index out of range
# 如果出现访问的数据超出列表范围，会报错 IndexError

print(nums[-1])
print(nums[2:])
print(nums[2:4]) #含头不含尾

print('+'*200)
names = ['mars','tony','eric']
print(names)

print('+'*200)
#疑问 是否在 列表中需要有同样的数据结构？

values = [5,6,0,'mars']
print(values)

print('+'*200)

#列表 数据的更改

print(nums)

#[25, 12, 36, 95, 14]
nums.append(45) #append [25, 12, 36, 95, 14, 45]
print(nums)

#关于数据插队

nums.insert(0,99) #insert [99, 25, 12, 36, 95, 14, 45]
print(nums)

nums.remove(14) #remove [99, 25, 12, 36, 95, 45]
print(nums)

#位置删除法
nums.pop(0) #pop [25, 12, 36, 95, 45]
print(nums)

print(nums[:2])

del nums[0] #del 可批量删除[36, 95, 45]
print(nums)

nums.extend([29,12,14,36]) #extend [36, 95, 45, 29, 12, 14, 36]
print(nums)

print('+'*200)

#统计
print(max(nums)) #max
print(min(nums)) #min

print(nums)
nums.sort() #sort 排序，默认从从小到大排序 除非后面加上reverse= true[12, 14, 29, 36, 36, 45, 95]
print(nums)

nums.reverse() #reverse 反转 [95, 45, 36, 36, 29, 14, 12]
print(nums)


nums.sort(reverse=True) #reverse [95, 45, 36, 36, 29, 14, 12]
print(nums)

str1='python'
print(list(str1))

print(nums.count(36)) #36在nums列表中有两个

print('*'*200)
lst = list(str1)
print(lst)

str2 = 'rust'
lst.extend(list(str2))
print(lst)

lst.sort()
print(lst)
