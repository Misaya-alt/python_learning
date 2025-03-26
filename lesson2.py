# 单引号，双引号，三引号定义法

name1 = 'I am a'
name2 = "I am b"
name3 = """I am c"""
print(name1,name2,name3)

# 在字符串内如果要有双引号，那就用单引号定义
# 如果要包含单引号，那就用双引号定义
# 也可使用转义字符\
name4 = '"I am d"'
name5 = "'I am e'"
name6 = "\"I am f\""
print(name4,name5,name6 )

# 字符串拼接用“+”，只能拼接字符串类型的变量
name7 = "Cat"
name8 = "mouse"
print(name7 + name8)

# 字符串格式化 %s， %为之后占位，s表示将占位的变量改成字符串
class_num = 57
avg_salary = 16781
message = "毕业生为%s期，平均工资为%s元" %(class_num,avg_salary)
print(message)
num = 2009060023
info = "刘圻浩是河南大学毕业生，学号为%s" % num
print(info)

# %s,%d,%f,分别占位并变成字符串，整数，浮点数
name = "company"
setup_year = 2010
num_year = 25.33
info = "公司名称为%s，成立于%d年，距今已有%f年的历史" % (name,setup_year,num_year)
print(info)

# 精度控制 m.n, m代表宽度，小数点占一位，n为小数位数，是四舍五入
num1 = 28371289
num2 =2139812.3213
print("将小数点控制在2位：%.2f" % num2)
print("将宽度控制在9位：%9d" % num1)
print("将宽度控制在15，小数点为3位：%15.3f" % num2)

# f"内容{变量}，快速占位并插入变量，不改变类型，也不做精度控制
name = "company"
setup_year = 2010
num_year = 25.33
print(f"公司名称为{name}，成立于{setup_year}年，距今已有{num_year}年的历史")

# 以上连接变量的方式同样适用于表达式，表达式就是有明确结果的式子，如1+1，type(x)等
print("1+1的结果是%d" % (1+1))
print(f"字符串在这里的类型是{type("1")}")
print("字符串在这里的类型是%s" % type("1"))

# 练习
name = "Lincombine1999"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
stock_price_after = stock_price_daily_growth_factor * stock_price * growth_days
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}元")
print("每日增长系数为%.2f，经过%d天的增长后，股价达到了%.2f元" %(stock_price_daily_growth_factor,growth_days,stock_price_after))

# 键盘的数据输入，input("提示消息")，括号里可以直接加字符串提示，输入的变量全都转化为了字符串
num = input("请输入你的学号")
print("你的学号类型是：",type(num))
num = int(num)
print(type(num))

# 练习
user_name = input("请告诉我您的名字")
user_type = input("请告诉我您的身份")
print(f"您好：{user_name},您是尊贵的{user_type}用户，欢迎您的光临")
print("您好，您是%s，是尊贵的%s，欢迎您的光临" %(user_name,user_type))