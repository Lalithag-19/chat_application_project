# client.py
import socket
import threading

server_ip = input("Enter server IP (or leave blank for localhost): ").strip()
if not server_ip:
    server_ip = "localhost"

server_port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("Disconnected from server.")
            break

def send_messages():
    while True:
        message = input()
        if message:
            client_socket.send(message.encode())

# Start receiving thread
receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

# Authenticate first
password = input()
client_socket.send(password.encode())

# Next, nickname and chatroom
nickname = input()
client_socket.send(nickname.encode())

room_code = input()
client_socket.send(room_code.encode())

# Then start sending messages
send_messages()
