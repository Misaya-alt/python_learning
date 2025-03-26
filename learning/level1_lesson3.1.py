# 布尔字符，可以通过直接赋值，比较运算符得到，==是否相等，!=是否不等
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1},类型是{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2},类型是{type(bool_2)}")

# ==,!=,也可用于字符串是否相等
print(f"10 == 10的结果是：{10 == 10}")
print(f"10 != 9的结果是：{10 != 9}")

"""if 要判断的条件：
    条件成立时要做的事（开头有四个缩进空格，表示归属某个if,可以有多行结果）"""
age1 = 30
if age1 >= 18:
    print("今年我成年了")
    print("我可以考驾照了")
print("这个不受上个if控制")

# 练习
print("Welcome to the world of MUJICA")
num = input("Please input your age")
age = int(num)
if age > 18:
    print("You have grown up,then you should pay more 10 yuan")
print("Have a good time!")

# if 312312:...else:...,lse与if同级，不用缩进,else不用再加条件
print("Welcome to the world of MUJICA")
num = input("Please input your age")
age = int(num)
if age > 18:
    print("You have grown up,then you should pay more 10 yuan")
else:
    print("You can enter ")
print("Have a good time!")

# 练习
print("欢迎来到上海")
height = int(input("请输入您的身高(cm)"))
if height > 120:
    print("您的身高超过120cm，游玩需要购票10元")
else:
    print("您的身高未超过120cm，可免费游玩")
print("祝您玩的愉快！")

# if...:,elif...:,else:，都是同级,else可省略
print("欢迎来到上海")
height = int(input("请输入您的身高(cm)"))
vip_level = int(input("请输入您的vip等级，只需输入数字"))
day = int(input("请告诉我今天几号"))
if height < 120:
    print("您的身高未超过120cm，可免费游玩")
elif vip_level >= 3:
    print(f"您是尊贵的vip{vip_level}用户，可免费游玩")
elif day == 1:
    print("今天是1号，可免费游玩")
else:
    print("您的身高超过120cm，需购票10元")
print("祝您玩的愉快！")
# 简化如下
if int(input("请输入您的身高(cm)")) < 120:
    print("您的身高未超过120cm，可免费游玩")
elif int(input("请输入您的vip等级，只需输入数字")) >= 3:
    print(f"您是尊贵的vip{vip_level}用户，可免费游玩")
elif int(input("请告诉我今天几号")) == 1:
    print("今天是1号，可免费游玩")
else:
    print("您的身高超过120cm，需购票10元")
print("祝您玩的愉快！")

num = 100
if int(input("请输入您猜的数字")) == num :
    print("不对")
elif int(input("再猜一次")) == num :
    print("不对")
elif int(input("再猜一次"))== num :
    print("不对")
else:
    print("三次全错，没机会了")