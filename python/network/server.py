from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random

# IP-Adresse und Port definieren
IP_ADDRESS = "127.0.0.1"
PORT = 8000

# Benutzerdefinierter Request-Handler
class RequestHandler(BaseHTTPRequestHandler):
    # Setze die Response-Header
    def _set_response(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    # Behandle POST-Anfragen
    def do_POST(self):
        # Content-Length erhalten und Post-Daten lesen
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        try:
            # Versuche, die JSON-Daten zu parsen
            json_data = json.loads(post_data)

            # Überprüfe, ob das JSON-Objekt die erforderlichen Schlüssel enthält
            required_keys = ["gameid", "gamerid", "positions", "colors", "value"]
            if not all(key in json_data for key in required_keys):
                raise ValueError("Ungültige JSON-Daten")
        except (json.JSONDecodeError, ValueError) as e:
            # Wenn das Parsen fehlschlägt, erforderliche Schlüssel fehlen oder "value" leer ist,
            # sende eine Fehlermeldung zurück
            self._set_response(400)
            response = {
                "error": str(e)
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        # gameid aus json_data erhalten
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

        # Setze die Response und sende sie zurück
        self._set_response()
        self.wfile.write(json.dumps(response).encode("utf-8"))


# Funktion zum Starten des Servers
def run_server():
    # Erstelle eine Serverinstanz mit der definierten Adresse und dem Request-Handler
    server_address = (IP_ADDRESS, PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server läuft auf {}:{}".format(IP_ADDRESS, PORT))
    # Beginne, Anfragen unbegrenzt zu bedienen
    httpd.serve_forever()


if __name__ == "__main__":
    # Starte den Server
    run_server()
