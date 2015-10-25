#-*-coding:utf-8-*-
#冒泡排序[百度百科](http://baike.baidu.com/link?url=4OvvH2FNEIO-QF3YmulKrEGoxFhCi_aXCKnxW4sJrwvd-UtUP8IvXRuh1BosPUsQDv2VP_1D5kfNqEUoc9g4Ia#3_14)
def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i+1]:
                bubbleList[i] = bubbleList[i] + bubbleList[i+1]
                bubbleList[i+1] = bubbleList[i] - bubbleList[i+1]
                bubbleList[i] = bubbleList[i] - bubbleList[i+1]
        listLength -= 1
    print bubbleList

if __name__ == '__main__':
    bubbleList = [3, 4, 1, 2, 5, 8, 0]
    bubble(bubbleList)