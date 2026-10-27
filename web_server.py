import http.server
import socketserver
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

print(f"Starting web server on port {PORT}...")
print("Press Ctrl+C in this pane to shut it down later.")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
	httpd.serve_forever()
