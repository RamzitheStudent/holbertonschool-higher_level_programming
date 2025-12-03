#!/usr/bin/python3
"""A simple HTTP server with multiple endpoints using http.server."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Request handler for a basic HTTP server."""

    def do_GET(self):
        """Handle GET requests."""
        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))

        # /data endpoint
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # /status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Undefined endpoints
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler,
        port=8000):
    """Starts the HTTP server on the specified port."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port {}...".format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()


if __name__ == "__main__":
    run()
