# if语句的嵌套，关键在于空格缩进
age = int(input("请输入您的年龄"))
# year = int(input("请输入您的在职时间"))
# level = int(input("请输入您的级别"))

if age >= 18:
    if age <= 30:
        if int(input("请输入您的在职时间")) >= 2:
            print("恭喜你")
        elif int(input("请输入您的级别")) >= 3:
            print("恭喜你")
        else:
            print("不好意思")
    else:
        print("不好意思")
else:
    print("不好意思")
