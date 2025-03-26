# if语句的嵌套，关键在于空格缩进
# age = int(input("请输入您的年龄"))
# # year = int(input("请输入您的在职时间"))
# # level = int(input("请输入您的级别"))
#
# if age >= 18:
#     if age <= 30:
#         if int(input("请输入您的在职时间")) >= 2:
#             print("恭喜你")
#         elif int(input("请输入您的级别")) >= 3:
#             print("恭喜你")
#         else:
#             print("不好意思")
#     else:
#         print("不好意思")
# else:
#     print("不好意思")

import random
print("我将会生成1到10的随机数，请你猜数字吧，每次输入的数字必须在此范围内且为整数")
num = random.randint(1,10)
num1 = int(input("请输入您猜的数字："))
if num1 > num:
    print("大了")
    num2 = int(input("请重新猜:"))
    if num2 > num:
        if int(input("大了，请重新猜:")) == num:
            print("对了")
        else:
            print("错了，没机会了")
    elif num2 < num:
        if int(input("小了，请重新猜:")) == num:
            print("对了")
        else:
            print("错了，没机会了")
    else:
        print("对了")
elif num1 < num:
    print("小了")
    num2 = int(input("请重新猜:"))
    if num2 > num:
        if int(input("大了，请重新猜:")) == num:
            print("对了")
        else:
            print("错了，没机会了")
    elif num2 < num:
        if int(input("小了，请重新猜:")) == num:
            print("对了")
        else:
            print("错了，没机会了")
    else:
        print("对了")
else:
    print("恭喜你，一次猜对！")
