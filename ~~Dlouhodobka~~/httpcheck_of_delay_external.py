import requests
import time
import socket

# Server configuration
server_ip = "176.16.1.10"
url = f"http://{server_ip}/index.html"
delay_threshold = 1.0  # Threshold in seconds
tcp_port = 10000  # Port to send alert messages

# Function to measure response time
def check_delay():
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            delay = end_time - start_time
            print(f"Response time: {delay:.2f} seconds")
            return delay
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

# Function to send alert to the server if delay is above threshold
def send_alert():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, tcp_port))
            s.sendall(b"Delay Exceeded")
            print("Alert sent to server!")
    except socket.error as e:
        print(f"Socket error: {e}")

# Main execution loop
if __name__ == "__main__":
    while True:
        delay = check_delay()
        if delay and delay > delay_threshold:
            print(f"Delay exceeded threshold of {delay_threshold} seconds!")
            send_alert()
            break  # Stop checking if alert is sent
        else:
            print("Delay is within acceptable range. Retrying in 1 second...\n")
            time.sleep(1)  # Wait for 1 second before retrying
