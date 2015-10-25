#-*-coding:utf-8-*-
import random
secret = random.randint(1,3)
#        print("卧槽，你是我心里的蛔虫吗？！")
#       print("哼，猜中了也没有奖励！")
#print("游戏结束，不玩了O(∩_∩)O哈哈~")

def r():
    print('--------------------------我的工作室-------------------')
    temp = input("不妨猜一下我现在心里想的是哪个数字：")
    guess = int(temp)
    #guess = int(temp)
    if guess == secret:
        print ( "gg,你是我的蛔虫吗？" )
        return
    if guess > secret:
        print( "gg,大了大了，再小点！" )
        r()
    else:
        print( "heihei,有点小哦，再猜" )
        r()



if __name__ == '__main__':
    print r()