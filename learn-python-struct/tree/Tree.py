"""
1 BinaryTree() 创建一个二叉树实例
2 getLeftChild() 返回当前节点的左子节点对应的二叉树
3 getRightChild() 返回当前节点的右子节点对应的二叉树
4 setRootVal(val) 在当前节点中存储参数val中的对象
5 getRootVal() 返回当前节点存储的对象
6 insertLeft(val) 新建一课二叉树，并将其作为当前节点的左子节点
7 insertRight(val) 新建一个二叉树，并将其作为当前节点的右子节点
"""

def BinaryTree(r):
    return [r, [], []]


'''
插入右子树
'''


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        # 将旧的的左子树 作为 新节点的左子树
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


'''
插入左子树
'''


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


'''
树的访问函数
'''


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]

r = BinaryTree(3)

insertLeft(r,4)

print(r)
