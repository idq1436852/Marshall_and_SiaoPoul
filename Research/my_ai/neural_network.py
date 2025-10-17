import numpy as np


# 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# sigmoid 的导数（用于反向传播）
def sigmoid_derivative(x):
    return x * (1 - x)


# 输入和输出 (训练数据)
# 训练数据：[0.1, 0.2, 0.3] -> 0 (小)；[0.8, 0.9] -> 1 (大)
X = np.array([
    [0.1],
    [0.2],
    [0.3],
    [0.8],
    [0.9]
])

y = np.array([
    [0],
    [0],
    [0],
    [1],
    [1]
])

# 初始化权重
np.random.seed(1)
# 1 输入 -> 3 隐藏层
weights_input_hidden = 2 * np.random.random((1, 3)) - 1
# 3 隐藏层 -> 1 输出
weights_hidden_output = 2 * np.random.random((3, 1)) - 1

# 训练网络
for i in range(10000):
    # 前向传播
    input_layer = X
    hidden_layer = sigmoid(np.dot(input_layer, weights_input_hidden))
    output_layer = sigmoid(np.dot(hidden_layer, weights_hidden_output))

    # 误差
    output_error = y - output_layer

    # 反向传播
    d_output = output_error * sigmoid_derivative(output_layer)
    hidden_error = d_output.dot(weights_hidden_output.T)
    d_hidden = hidden_error * sigmoid_derivative(hidden_layer)

    # 更新权重
    weights_hidden_output += hidden_layer.T.dot(d_output)
    weights_input_hidden += input_layer.T.dot(d_hidden)


# 测试函数
def predict(x):
    hidden = sigmoid(np.dot(x, weights_input_hidden))
    output = sigmoid(np.dot(hidden, weights_hidden_output))
    return "大 😎" if output > 0.5 else "小 🙈"


# 用户测试
while True:
    try:
        user_input = float(input("请输入一个 0~1 之间的数字 (输入 -1 退出): "))
        if user_input == -1:
            print("小宝：爱你哦~下次见 Muah~💋")
            break

        x = np.array([[user_input]])
        print(f"小宝判断: {predict(x)}")
    except:
        print("输入不合法哦宝~再试一次🥺")
