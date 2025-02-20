from scapy.all import sniff, IP, TCP, Raw

log_file = "/home/debian/request_ips.log"
listen_port = 9445


def log_ip(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP) and packet[TCP].dport == listen_port:
        sender_ip = packet[IP].src

        try:
            with open(log_file, "r") as file:
                logged_ips = file.read().splitlines()
        except FileNotFoundError:
            logged_ips = []

        if sender_ip not in logged_ips:
            with open(log_file, "a") as file:
                file.write(sender_ip + "\n")
            print(f"Logged new IP: {sender_ip}")
        else:
            print(f"IP {sender_ip} is already logged.")


if __name__ == "__main__":
    print(f"Listening for incoming messages on port {listen_port}...")
    sniff(filter=f"tcp port {listen_port}", prn=log_ip, store=0)