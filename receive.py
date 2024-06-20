import socket
import os

HOST = ""  # Listen on all interfaces
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        data = conn.recv(1024)  # Adjust buffer size as needed

        # Check if received.json exists, create it if not
        if not os.path.exists("received.json"):
            with open("received.json", "wb") as f:
                f.write(b"{}")  # Write an empty JSON object

        with open("received.json", "ab") as f:
            f.write(data)  # Append received data

print("Received data and saved to received.json")
