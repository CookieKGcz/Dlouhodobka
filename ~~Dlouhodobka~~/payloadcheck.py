from scapy.all import send, IP, TCP, Raw

target_ip = "176.16.1.21"
target_port = 9445  # Port where the logging script listens


def send_http_message():
    payload = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_ip)
    packet = IP(dst=target_ip) / TCP(dport=target_port, sport=12345, flags="PA") / Raw(load=payload)

    send(packet)
    print(f"Sent HTTP message to {target_ip}")


if __name__ == "__main__":
    send_http_message()