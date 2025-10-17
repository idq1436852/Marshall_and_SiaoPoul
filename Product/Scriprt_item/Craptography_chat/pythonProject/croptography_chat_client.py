import socket
from cryptography.fernet import Fernet

# 读取密钥
with open("/storage/emulated/0/ItsBelongfMe/lab/secret/secret.key", "rb") as f:
    key = f.read()
    cipher = Fernet(key)

# 连接服务器
client = socket.socket()
client.connect(("192.168.4.15", 12345))  # 请注意，这里的 IP 地址可能需要替换成你服务器的实际 IP 哦！
print("✅ 已连接到服务器！")

# 循环发送消息
while True:
    msg = input("请输入要发送的消息: ")
    if not msg:
        print("🛑 连接已断开。")
        break

    # 加密并发送
    encrypted = cipher.encrypt(msg.encode())
    client.send(encrypted)

    # 接收服务器返回的加密消息
    try:
        data = client.recv(1024)
        if not data:
            print("⚠️ 服务器已断开连接。")
            break

        decrypted = cipher.decrypt(data).decode()
        print("服务器回复:", decrypted)

    except Exception as e:
        print("⚠️ 解密失败:", e)
        break

client.close()
print("❌ 客户端已关闭。")
