import socket

# Replace with your file path and receiver IP
file_path = "data.json"
HOST = "192.168.1.8"  # Replace with receiver's IP address
PORT = 65432        # Choose an unused port number

with open(file_path, "rb") as f:
    data = f.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data)

print("Sent data from", file_path)
