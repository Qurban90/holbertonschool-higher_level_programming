#!/usr/bin/env python3
"""
Simple HTTP server using http.server module
Handles multiple endpoints and serves JSON data
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler
    """

    def do_GET(self):
        """
        Handle GET requests
        """
        # Default headers
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Root endpoint
        if self.path == "/":
            message = {"message": "Hello, this is a simple API!"}
            self.wfile.write(json.dumps(message).encode("utf-8"))

        # /data endpoint
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # /status endpoint
        elif self.path == "/status":
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode("utf-8"))

        # Undefined endpoints
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Run the HTTP server
    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    print("Visit http://localhost:8000 in your browser")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()


if __name__ == "__main__":
    run()
