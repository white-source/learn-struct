# -*- coding: utf-8 -*-


tup1 = ('a', 'b', 10, 20)
tup2 = (1, 2, 3, 4, 5 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:4]: ", tup2[1:4])


tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)

tup = ('a', 'b', 10, 20)
print (tup)
del tup
print ("删除后的结果: ")
#print (tup)


tup1 = (1,2,3)
tup2 = (4,5,6)
print(len(tup1))
print(tup1+tup2)
print(tup1*3)
print(3 in tup1)	
for x in tup1: 
    print (x)