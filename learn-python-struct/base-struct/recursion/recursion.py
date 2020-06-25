from turtle import *

from pythonds import Stack


def listSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])


def toStr(n, base):
    converString = "0123456789ABCDEF"
    if n < base:
        return converString[n]
    else:
        return toStr(n // base, base) + converString[n % base]


rStack = Stack()


def toStrStack(n, base):
    converString = "0123456789ABCDEF"
    if n < base:
        return converString[n]
    else:
        # 我就卡在这一步了
        rStack.push(converString[n % base])
        return toStrStack(n // base, base)


if __name__ == '__main__':
    print(toStr(10, 2))
