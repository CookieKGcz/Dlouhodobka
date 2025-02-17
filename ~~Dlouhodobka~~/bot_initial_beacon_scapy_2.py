from scapy.all import send, sniff, IP, TCP, Raw

def send_get_request(port, endpoint="/"):
    ip = "10.2.1.10"
    payload = f"GET {endpoint} HTTP/1.1\r\nHost: {ip}\r\n\r\n"
    packet = IP(dst=ip)/TCP(dport=int(port), sport=12345, flags="S")/Raw(load=payload)
    send(packet)
    print(f"Sent HTTP GET request to {ip}:{port}{endpoint}")

    print("Waiting for response...")
    sniff(filter=f"tcp and src host {ip} and src port {port}", prn=handle_response, timeout=5, store=0, count=3)

def handle_response(packet):
    if packet.haslayer(Raw):
        response = packet[Raw].load.decode(errors='ignore')
        print("Received Response:")
        print(response) # prints the payload

if __name__ == "__main__":
    port = input("Enter the port: ")
    endpoint = input("Enter the endpoint (default is /): ") or "/"
    send_get_request(port, endpoint)