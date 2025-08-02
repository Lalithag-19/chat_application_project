import mysql.connector
from datetime import datetime

# MySQL connection config
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "*******",
    "database": "chatdb"   # Make sure you created this database first
}

# Initialize table
def initialize_database():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp VARCHAR(255),
            room_code VARCHAR(255),
            sender_ip VARCHAR(255),
            message TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Insert a message
def log_message(room_code, sender_ip, message):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    timestamp = datetime.utcnow().isoformat()
    sql = """
        INSERT INTO messages (timestamp, room_code, sender_ip, message)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (timestamp, room_code, sender_ip, message))
    conn.commit()
    cursor.close()
    conn.close()

# Create table if needed
initialize_database()
