from http.server import BaseHTTPRequestHandler, HTTPServer

target_port = 9443
log_file = "request.log"


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]

        with open(log_file, "a") as file:
            file.write(client_ip + "\n")

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"IP logged successfully\n")


if __name__ == "__main__":
    server = HTTPServer(("", target_port), RequestHandler)
    print(f"Server running on port {target_port}...")
    server.serve_forever()
