# 通过print语句输出字面量

print("hello world")
print(666)
print(14.14)


# 定于一个变量，记录钱包余额
money = 50
# 通过print输出money，逗号表示可以一起输出后面的内容
print("钱包还有：",money,"元")

#买了一个东西，花了10元
money = money - 10
print("买了东西还剩：",money,"元")

# 练习
money = 50
icecream = 10
cola = 5
print("当前钱包余额：",money,"元")
print("买冰淇淋花了：",icecream,"元")
print("买可乐花了：",cola,"元")
money = money - icecream - cola
print("最终，还剩：",money,"元")
# 练习结束

# type() 查看数据类型，变量没有类型
name="liuqihao"
print(type("1111"))
print(type(name))

#数据变量类型转化，int(x),float(x),str(x)
num_str = str(11)
print(type(num_str),num_str)
print(type(str(money)))
num1 = int("11")
print(type(num1))
num2 = float("11")
print(type(num2),num2)

# 整数转浮点数可以，浮点数转整数也可，但小数部分会丢失
int1 = int(11.11)
print(type(int1),int1)

# //整除，%取余，**指数
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# +=,加后面的数字之后赋值到本身
num4 = 5  # 或者其他合适的初始值
num4 += 3
print(num4)

