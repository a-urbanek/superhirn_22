import json
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

IP_ADDRESS = "127.0.0.1"
PORT = 8000


class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        try:
            json_data = json.loads(post_data)

            required_keys = ["gameid", "gamerid", "positions", "colors", "value"]
            if not all(key in json_data for key in required_keys):
                raise ValueError("Ungültige JSON-Daten")
        except (json.JSONDecodeError, ValueError) as e:
            self._set_response(400)
            response = {
                "error": str(e)
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        gameid = json_data.get("gameid")
        positions = json_data.get("positions")
        colors = json_data.get("colors")
        gamerid = json_data.get("gamerid")

        if gameid == 0:
            gameid = random.randint(1, 10000)

        response = {
            "gameid": gameid,
            "gamerid": gamerid,
            "positions": positions,
            "colors": colors,
            "value": ''.join(random.sample("12345678", colors))
        }

        self._set_response()
        self.wfile.write(json.dumps(response).encode("utf-8"))


def run_server():
    server_address = (IP_ADDRESS, PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server läuft auf {}:{}".format(IP_ADDRESS, PORT))
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
