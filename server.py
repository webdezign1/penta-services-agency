import http.server
import socketserver
import os
import json
import mimetypes
from urllib.parse import urlparse, parse_qs
from datetime import datetime

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")

LEADS_FILE = os.path.join(DIRECTORY, "leads.json")

class PentaHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # API: Geo / Currency
        if path == "/api/geo.php":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({
                "country": "GB",
                "currency": "GBP",
                "pkr": None
            }).encode("utf-8"))
            return

        # API: OAuth providers
        if path == "/api/oauth/providers":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({
                "ok": True,
                "providers": ["google", "microsoft"]
            }).encode("utf-8"))
            return

        # API: Account / Leads view
        if path == "/api/leads":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            if os.path.exists(LEADS_FILE):
                with open(LEADS_FILE, "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))
            else:
                self.wfile.write(b"[]")
            return

        # Resolve local file
        clean_path = path.lstrip("/")
        local_target = os.path.join(DIRECTORY, clean_path.replace("/", os.sep))

        if os.path.isfile(local_target):
            return super().do_GET()

        # SPA Routing: Any /<lang>/... or pretty route serves index.html
        if path.startswith("/en/") or path.startswith("/it/") or path.startswith("/fr/") or path.startswith("/ar/") or path.startswith("/zh/") or path in ["/", "/index.html", "/services", "/pricing", "/cart"]:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            index_path = os.path.join(DIRECTORY, "index.html")
            with open(index_path, "rb") as f:
                self.wfile.write(f.read())
            return

        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path in ["/api/send.php", "/api/send"]:
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            
            try:
                data = json.loads(post_data)
            except Exception:
                data = {"raw": post_data}

            record = {
                "id": f"PENTA-{int(datetime.now().timestamp()*1000)}",
                "received_at": datetime.now().isoformat(),
                "payload": data
            }

            # Append to leads.json
            leads = []
            if os.path.exists(LEADS_FILE):
                try:
                    with open(LEADS_FILE, "r", encoding="utf-8") as f:
                        leads = json.load(f)
                except Exception:
                    leads = []
            leads.append(record)
            with open(LEADS_FILE, "w", encoding="utf-8") as f:
                json.dump(leads, f, indent=2, ensure_ascii=False)

            # Response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({
                "ok": True,
                "id": record["id"],
                "message": "Inquiry successfully recorded."
            }).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

if __name__ == "__main__":
    print(f"==================================================")
    print(f"   Penta Services Web Application Server")
    print(f"   Running at http://localhost:{PORT}/")
    print(f"   Direct URL: http://localhost:{PORT}/en/")
    print(f"==================================================")
    with socketserver.TCPServer(("", PORT), PentaHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
