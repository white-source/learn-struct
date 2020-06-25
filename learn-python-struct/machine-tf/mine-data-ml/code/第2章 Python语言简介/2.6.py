# -*- coding: utf-8 -*-


dict = {'a': 1, 'b': 2, 'b': '3'}
print(dict['b'])
print(dict)


dict = {'Name': 'xioaming', 'Age': 20, 'Class': 'First'};
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


dict = {'Name': 'xioaming', 'Age': 20, 'Class': 'First'} 
#print ("dict[xiaowang']: ", dict['xiaowang'])



dict = {'Name': 'xioaming', 'Age': 20, 'Class': 'First'};
dict['Age'] = 22; # 修改年龄
dict['School'] = "NUIST"; # 添加新的键/值对
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


dict = {'Name': 'xioaming', 'Age': 20, 'Class': 'First'}
del dict['Name'] # 删除键是'Name'的条目
dict.clear()     # 清空词典所有条目
del dict        # 删除词典
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])