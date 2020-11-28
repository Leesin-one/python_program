# 原有1000元存款，发工资后变为2000元
# money.py

money=1000
def send():
    global money
    money=2000
def select():
    if money==1000:
        print(f"没发工资，原来余额为{money}")
    elif money==2000:
        print("发工资了，工资余额为{}".format(money))
    else:
        print("出现错误了")

if __name__=="__main__":
    # send()
    select()


