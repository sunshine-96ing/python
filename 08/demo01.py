dict1 = {}

print(dict1)

dict2 = {'key1':'100','key2':200}
print(dict2)
print(dict2['key1'])
print(dict2['key2'])

dict2 = {'key1':30,'key2':50,'key3':100}
print(len(dict2))

dict2['key1']=150 #{'key1': 150, 'key2': 50, 'key3': 100}
print(dict2)

dict2['key4']=200 #{'key1': 150, 'key2': 50, 'key3': 100, 'key4': 200}
print(dict2)

del dict2['key4'] #{'key1': 150, 'key2': 50, 'key3': 100}
print(dict2)

print('**'*100)
dict2 = {'key1':30,'key2':50,'key3':100}
dict3 = {'key3':100,'key2':50,'key1':30}

import operator
print(operator.eq(dict2,dict3))

print('**'*100)
list1=[80,84,87]
list2=[90,81,75]
dict4={}
dict4['语文']=list2
dict4['数学']=list1
print(dict4)

print(dict4['语文'][0])
print(dict4.keys())
print(dict4.values())

#key列表和value列表的组合
print('**'*100)
list1=['key1','key2','key3']
list2=[30,50,100]

dict5=dict.fromkeys(list1,list2) #fromkeys {'key1': [30, 50, 100], 'key2': [30, 50, 100], 'key3': [30, 50, 100]}
print(dict5)

dict6=dict(zip(list1,list2)) #zip {'key1': 30, 'key2': 50, 'key3': 100}
print(dict6)


#print(dict4['英语']) 报错

print('英语'in dict4) #False
print(dict4.get('英语','不存在')) #不存在
print(dict4.get('数学','不存在')) #[80, 84, 87]

#作业

# s=input('输入所在的国家和首都，用逗号隔开')
# print(s)

# list= s.split(',')
# print(list)
print('**'*100)

dict7={'中国':"北京"}
a=input('输入所在的国家')
print(a+','+dict7[a])