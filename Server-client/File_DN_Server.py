import http.server
import socketserver

PORT = 8000
DIRECTORY = '/path/to/files'

Handler = http.server.SimpleHTTPRequestHandler
Handler.directory = DIRECTORY

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
