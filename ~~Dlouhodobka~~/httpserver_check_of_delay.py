import requests
import time

server_ip = "176.16.1.10"
url = f"http://{server_ip}/index.html"
delay_threshold = 1.0  # Threshold
string_to_append = "<!-- High latency detected! -->"

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

# Function to append a string to index.html if delay is above threshold
def append_to_file():
    try:
        with open("/var/www/html/index.html", "a") as file:  # Adjust path if needed
            file.write(string_to_append + "\n")
        print("Appended string to index.html")
    except FileNotFoundError:
        print("Error: index.html not found.")
    except PermissionError:
        print("Error: Insufficient permissions to modify index.html.")

# Main execution
if __name__ == "__main__":
    delay = check_delay()
    if delay and delay > delay_threshold:
        print(f"Delay exceeded threshold of {delay_threshold} seconds!")
        append_to_file()
    else:
        print("Delay is within acceptable range.")