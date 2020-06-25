str1 = 'Hello World!'
str2 = "Python"
print(str1)
print(str2)
print ("str1[0]: ", str1[0])
print ("str2[1:5]: ", str2[1:5])




str1 = 'Hello '
str2 = 'world!'
str1 = str1+str2
print(str1)



a = "Hello"
b = "Python"
print ("a + b 输出结果：", a + b)
print ("a * 2 输出结果：", a * 2)
print ("a[1] 输出结果：", a[1])
print ("a[1:4] 输出结果：", a[1:4])
if( "H" in a) :
    print ("H 在变量 a 中")
else :
    print ("H 不在变量 a 中")
if( "N" not in a) :
    print ("N 不在变量 a 中")
else :
    print ("N 在变量 a 中")
    
print ("My name is %s and age is %d!" % ('xiaoming', 20))