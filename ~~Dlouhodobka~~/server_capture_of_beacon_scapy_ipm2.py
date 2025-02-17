from scapy.all import sniff, IP, TCP, Raw, send

target_port = 9443
log_file = "request_ips.log"
response_file = "response_content.txt"


def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP) and packet.haslayer(Raw):
        if packet[TCP].dport == target_port:
            client_ip = packet[IP].src
            payload = packet[Raw].load.decode(errors='ignore')
            if payload.startswith("GET"):
                try:
                    with open(log_file, "r") as file:
                        logged_ips = file.read().splitlines()
                except FileNotFoundError:
                    logged_ips = []

                if client_ip not in logged_ips:
                    with open(log_file, "a") as file:
                        file.write(client_ip + "\n")
                    print(f"Logged IP: {client_ip}")

                # Read response content from local file
                try:
                    with open(response_file, "r") as file:
                        response_content = file.read()
                except FileNotFoundError:
                    response_content = "File not found."

                # Construct HTTP response packet
                response_payload = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_content)}\r\n\r\n{response_content}"
                response_packet = IP(dst=client_ip) / TCP(dport=packet[TCP].sport, sport=target_port, flags="PA") / Raw(
                    load=response_payload)
                send(response_packet)
                print(f"Sent response to {client_ip}")


if __name__ == "__main__":
    print(f"Listening for HTTP GET requests on port {target_port}...")
    sniff(filter=f"tcp port {target_port}", prn=packet_callback, store=0)