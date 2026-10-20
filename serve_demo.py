from pathlib import Path
import http.server, socketserver, webbrowser, os
ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass
with socketserver.TCPServer(("127.0.0.1",0), Handler) as httpd:
    port=httpd.server_address[1]
    url=f"http://127.0.0.1:{port}/index.html"
    print(f"Programme Evidence Hub demonstrator running at {url}")
    print("Press Ctrl+C to stop.")
    webbrowser.open(url)
    try: httpd.serve_forever()
    except KeyboardInterrupt: pass
