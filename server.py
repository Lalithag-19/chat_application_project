# server.py
import socket
import threading
from database import log_message
from config import HOST, PORT

chatrooms = {}  # { room_code: [(client_socket, nickname)] }
chatrooms_lock = threading.Lock()

SERVER_PASSWORD = "chat@123"

def handle_client(client_socket, client_address):
    try:
        # Ask for password
        client_socket.send(b"Enter server password: ")
        password = client_socket.recv(1024).decode().strip()

        if password != SERVER_PASSWORD:
            client_socket.send(b"Invalid password. Disconnecting.\n")
            client_socket.close()
            return

        # Ask for nickname
        client_socket.send(b"Enter your nickname: ")
        nickname = client_socket.recv(1024).decode().strip()

        # Ask for chatroom code
        client_socket.send(b"Enter chatroom code to create/join: ")
        room_code = client_socket.recv(1024).decode().strip()

        with chatrooms_lock:
            if room_code not in chatrooms:
                chatrooms[room_code] = []
            chatrooms[room_code].append((client_socket, nickname))

        client_socket.send(f"Joined chatroom '{room_code}'. Start chatting!\n".encode())

        while True:
            message = client_socket.recv(1024).decode().strip()
            if not message:
                break

            log_message(room_code, nickname, message)

            broadcast_message = f"[{nickname}] {message}"
            broadcast_to_room(room_code, broadcast_message, client_socket)

    except ConnectionResetError:
        print(f"Connection lost from {client_address}")
    finally:
        with chatrooms_lock:
            if room_code in chatrooms:
                chatrooms[room_code] = [
                    (c, n) for c, n in chatrooms[room_code] if c != client_socket
                ]
                if not chatrooms[room_code]:
                    del chatrooms[room_code]
        client_socket.close()

def broadcast_to_room(room_code, message, sender_socket):
    with chatrooms_lock:
        for client, _ in chatrooms.get(room_code, []):
            if client != sender_socket:
                try:
                    client.send((message + "\n").encode())
                except:
                    pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"New connection from {addr}")
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, addr), daemon=True
        )
        client_thread.start()

if __name__ == "__main__":
    start_server()
