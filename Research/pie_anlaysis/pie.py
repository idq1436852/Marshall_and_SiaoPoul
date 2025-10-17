import matplotlib.pyplot as plt
import random
import time

labels = ['A', 'B', 'C', 'D']

# 打开交互模式，让图可以动态更新
plt.ion()

for _ in range(20):  # 循环 20 次模拟变化
    # 随机生成数据
    sizes = [random.randint(1, 10) for _ in labels]

    plt.clf()  # 清空当前图
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("动态饼图示例")
    plt.pause(0.5)  # 暂停 0.5 秒

# 关闭交互模式，保持最后一个图表显示（可选）
plt.ioff()
plt.show()
