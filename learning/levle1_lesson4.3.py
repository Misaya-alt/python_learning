# for循环
"""for 临时变量 in 待处理数据集
    循环满足条件时执行的代码"""

name = "liuiqihao"
for x in name:
    # 将name中的内容依次取出赋值给临时变量x
    # 然后在循环体中对x进行处理
    print(x)

count = 0
name = "itheima is a brand of itcast"
for i in name:
    if i == "a":
        count += 1
    else:
        count = count
print(f"里面一个有{count}个a")
print()