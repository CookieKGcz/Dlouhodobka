import requests

def send_get_request(port, endpoint="/"):
    ip = "10.2.1.10"
    url = f"http://{ip}:{port}{endpoint}"
    try:
        response = requests.get(url)
        print(f"Response Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    port = input("Enter the port: ")
    endpoint = input("Enter the endpoint (default is /): ") or "/"
    send_get_request(port, endpoint)

