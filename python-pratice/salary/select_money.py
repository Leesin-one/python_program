# 判断money的值，从而显示余额
import money
def select():
    if money.money==1000:
        print("没发工资，原来余额为{}".format(money.money))
    elif money.money==2000:
        print("发工资了，工资余额为{}".format(money.money))
    else:
        print("出现错误了")