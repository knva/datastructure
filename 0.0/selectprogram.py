import datetime

#问题:设有一组N个数,而要确定其中第K 个最大者,
#思路 先排序,然后变换为递减顺序,返回第K个元素
def getMaxNum(num,key):
    maxNum = 0
    num.sort()
    num.reverse()
    print(num)
    for index in range(len(num)):
        if((key-1)==index):
            maxNum =num[index]
    return maxNum




#思路2 先获取前K个元素,然后在逐个匹配
def getMaxNumByKey(num,key):
    maxNum = 0
    pNum = []
    for index in range(len(num)):
        if(index<key):
            pNum.append(num[index])
    pNum.sort()
    pNum.reverse()
    print(pNum)
    mNum = num
    del mNum[0:key-1]
    for index in range(len(mNum)):
        if(mNum[index]>pNum[key-1]):
            pNum.append(mNum[index])
            pNum.sort()
            pNum.reverse()
            pNum.pop()
    print(pNum)
    return pNum[key-1]



number = [3,2,1,43,6,7,8,94,34,54,423,412,4,5,43,143,431,51,66,77,22,99,194,392,491,432]
start = datetime.datetime.now()
maxNum = getMaxNumByKey(number,15)
end = datetime.datetime.now()
print(maxNum)
print (end-start)
