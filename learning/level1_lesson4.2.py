# while嵌套
i = 1
while i <= 100:
    print(f"这是我第{i}天学习python")
    j = 5
    while j != 0:
        print(f"还剩{j}天，努力学习！")
        j -= 1
    print("结束力")
    i += 5
print("学了100天")

# 乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end = '')
        j +=1
    i += 1
    print()



