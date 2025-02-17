from scapy.all import sniff, IP, TCP, Raw

target_port = 9443
log_file = "request_ips.log"

def packet_callback(packet):
    if packet.haslayer("IP") and packet.haslayer("TCP") and packet.haslayer("Raw"):
        if packet["TCP"].dport == target_port:
            client_ip = packet["IP"].src
            payload = packet["Raw"].load.decode(errors='ignore')
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


if __name__ == "__main__":
    print(f"Listening for HTTP GET requests on port {target_port}...")
    sniff(filter=f"tcp port {target_port}", prn=packet_callback, store=0)