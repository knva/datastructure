def getMaxNum(num,key):
    maxNum = 0
    num.sort()
    num.reverse()
    print(num)
    for index in range(len(num)):
        if((key-1)==index):
            maxNum =num[index]
    return maxNum

number = [3,2,1,43,6,7,8,94,34,54]
maxNum = getMaxNum(number,1)
print(maxNum)
