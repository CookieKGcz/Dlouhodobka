import socket

# Server configuration
host = "0.0.0.0"  # Listen on all available interfaces
tcp_port = 10000   # Port to listen on

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, tcp_port))
    server_socket.listen(5)
    print(f"Listening for alerts on port {tcp_port}...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connection established from {addr}")
            message = conn.recv(1024).decode()
            if message == "Delay Exceeded":
                print("Received alert: Delay is over the threshold!")