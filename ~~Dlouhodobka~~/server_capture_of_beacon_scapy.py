from scapy.all import sniff

target_port = 9443
log_file = "request_ips.log"

def packet_callback(packet):
    if packet.haslayer("IP") and packet.haslayer("TCP"):
        if packet["TCP"].dport == target_port:
            client_ip = packet["IP"].src
            with open(log_file, "a") as file:
                file.write(client_ip + "\n")
            print(f"Logged IP: {client_ip}")

if __name__ == "__main__":
    print(f"Listening for HTTP GET requests on port {target_port}...")
    sniff(filter=f"tcp port {target_port}", prn=packet_callback, store=0)