# while 条件：
#     条件满足时，...
#     条件满足时，...
#     ....

i = 0
while i < 2:
    print("hello world")
    i += 1

i = 1
s = 0
while i <= 2:
    s += i
    i += 1
print(i,s)

# 猜数字
import  random
num = random.randint(1,100)
i = 1
guess = int(input("请输入你猜的数字："))
while guess != num:
    i += 1
    if guess > num:
        guess = int(input("猜大了，请重新猜"))
    else:
        guess = int(input("猜小了，请重新猜"))
print(f"恭喜你猜中了，数字是{num},一共猜了{i}次")

import random
result = True
num = random.randint(1, 100)
i = 0
while result :
    guess = int(input("请输入你猜的数字"))
    i += 1
    if guess == num:
        print("恭喜你猜对了")
        result = False
    elif guess < num:
        print("猜小了")
    else:
        print("猜大了")
print(f"你一共猜了{i}次")