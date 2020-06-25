# -*- coding: utf-8 -*-

list1 = ['a', 'b', 10, 20]
list2 = [1, 2, 3, 4]
print ("list1[0]: ", list1[0])
print ("list2[1:4]: ", list2[1:4])

list = []               # 空列表
list.append('Hello')   # 使用 append() 添加元素
list.append('World!')
print (list)


list1 = ['a', 'b', 10, 20]
print (list1)
del list1[2]
print ("删除后的输出为 : ")
print (list1)

list1 = [1,2,3]
list2 = [4,5,6]
print(len(list1))
print(list1+list2)
print(list1*3)
print(3 in list1)	
for x in list1: 
    print (x)