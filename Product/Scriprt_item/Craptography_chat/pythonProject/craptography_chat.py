import socket
from cryptography.fernet import Fernet

with open("secret.key", "rb") as f:
    key = f.read()
    cipher = Fernet(key)

server = socket.socket()
server.bind(("0.0.0.0", 12345))
server.listen(1)
print("The server is staring, waiting for connect")

conn, addr = server.accept()
print(f"This connect is from {addr}")

while True:
    data = conn.recv(4096)
    if not data:
        break
    decrypted = cipher.decrypt(data)
    print("Get the massage", decrypted.decode())

    messages = input("What are you gonna say: ")
    encrypted = cipher.encrypt(messages.encode())
    conn.send(encrypted)

conn.close()
