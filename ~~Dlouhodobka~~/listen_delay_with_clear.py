import socket
import time

# Server configuration
host = "0.0.0.0"  # Listen on all available interfaces
tcp_port = 10000  # Port to listen on
index_file = "/var/www/html/index.html"

# Flags to append
http_string_to_append = "flag{http_flood_?4a6sd3}"
tcp_string_to_append = "flag{tcp_flood_?564as3}"

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

            # Check for HTTP delay alert
            if message == "HTTP Delay Exceeded":
                print("Received alert: HTTP Delay is over the threshold!")
                try:
                    with open(index_file, "a") as file:
                        file.write(http_string_to_append + "\n")
                    print("Appended HTTP flag to index.html")
                except FileNotFoundError:
                    print("Error: index.html not found.")
                except PermissionError:
                    print("Error: Insufficient permissions to modify index.html.")

            # Check for TCP delay alert
            if message == "TCP Delay Exceeded":
                print("Received alert: TCP Delay is over the threshold!")
                try:
                    with open(index_file, "a") as file:
                        file.write(tcp_string_to_append + "\n")
                    print("Appended TCP flag to index.html")
                except FileNotFoundError:
                    print("Error: index.html not found.")
                except PermissionError:
                    print("Error: Insufficient permissions to modify index.html.")

            # Check if both flags are in the file
            try:
                with open(index_file, "r") as file:
                    content = file.read()

                if http_string_to_append in content and tcp_string_to_append in content:
                    print("Both flags detected in index.html. Waiting 20 seconds before removing flags...")
                    time.sleep(20)  # Wait for 20 seconds

                    # Remove the last X characters where X is the length of the flags
                    with open(index_file, "rb+") as file:
                        file.seek(0, 2)  # Go to the end of the file
                        file_size = file.tell()

                        # Calculate the number of characters to remove
                        chars_to_remove = len(http_string_to_append) + len(tcp_string_to_append) + 2  # +2 for newlines
                        new_size = max(0, file_size - chars_to_remove)

                        file.truncate(new_size)
                    print(f"Removed last {chars_to_remove} characters (flags) from index.html")
            except FileNotFoundError:
                print("Error: index.html not found during flag check.")