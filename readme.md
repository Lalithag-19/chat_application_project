# Python Chat Room Application

This is a **Python socket-based chat room project** that allows multiple users to connect to a server, join or create chat rooms, and exchange messages in real time.

## ✨ Features

✅ **Multi-user chat rooms**
- Multiple users can join the same room and chat together.
- Each room is identified by a unique code.

✅ **Multiple rooms**
- You can create or join any number of rooms independently.

✅ **Nickname support**
- Users choose a nickname when connecting.
- Messages display nicknames instead of IP addresses.

✅ **Password authentication**
- Server requires a password (`chat@123`) for clients to connect, improving security.

✅ **Persistent message storage in MySQL**
- All chat messages are stored in a **MySQL database** for later retrieval and record-keeping.

✅ **Cross-system support**
- Clients can connect from different machines on the same network (LAN).

✅ **Simple and clean design**
- Modular server and client code.
- Easy to extend or adapt for further features.

---

## 🛠️ How to Run

### 1️⃣ Requirements

- Python 3.x installed on all systems.
- Local network connectivity (same Wi-Fi or LAN).
- A MySQL server running and accessible.
- Python MySQL connector installed (`pip install mysql-connector-python`).

### 2️⃣ MySQL Setup

1. **Create a database**, e.g., `chatdb`.
2. **Create a table** to store messages:

   ```sql
   CREATE TABLE messages (
       id INT AUTO_INCREMENT PRIMARY KEY,
       room VARCHAR(255),
       timestamp DATETIME,
       sender VARCHAR(255),
       content TEXT
   );



