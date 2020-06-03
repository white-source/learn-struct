# 随机生成一个整数列表
import random

# randomList = [random.choice(range(1,x)) for x in range(20,30)]
# print(randomList)


randomListData = [1, 3, 21, 16, 2, 6, 22, 10, 7, 10]


# 1 遍历 两两交换 找出最大的那个 元素 放在后面
# 2 先写内层的循环，再写外层的循环
# 3  学习可视化网站 https://visualgo.net/en/sorting
def bubblesort(randomList):
    for j in range(len(randomList)):
        for i in range(len(randomList)-j):
            if i+1 < len(randomList) and randomList[i] > randomList[i + 1] :
                temp = randomList[i]
                randomList[i] = randomList[i + 1]
                randomList[i + 1] = temp
        print(randomList)


bubblesort(randomListData)



