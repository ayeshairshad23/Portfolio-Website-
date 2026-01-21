#!/usr/bin/env python3
"""
Simple HTTP Server for Portfolio Website
No Node.js required! Just Python.
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 3000
HANDLER = http.server.SimpleHTTPRequestHandler

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def run_server():
    """Start the HTTP server"""
    # Change to the directory containing this script
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print("🌟 Portfolio Website Server Running!")
        print("=" * 60)
        print(f"📍 Open your browser at: {url}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print("⏹️  Press Ctrl+C to stop the server")
        print("=" * 60)
        
        # Open browser automatically
        try:
            webbrowser.open(url)
            print(f"✅ Browser opened at {url}")
        except:
            print(f"⚠️  Please open {url} in your browser manually")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped. Goodbye!")
            exit(0)

if __name__ == "__main__":
    run_server()
