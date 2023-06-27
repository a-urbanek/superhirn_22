import json

import requests

from config import config
from config import game_config


class ComputerNetworkCoder:
    def __init__(self):
        # Initialisierung der Variablen
        self.gameid = 0
        self.gamerid = "Gruppe 22"
        self.positions = config.COLUMNS
        self.colors = len(config.COLORS)
        self.value = ""

        # Senden eines Requests an den Server, um das Spiel zu initialisieren
        self.send_request(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        print("Game ID:", self.gameid)
        print(self.colors)

        if self.gameid != 0:
            # Der Geheimcode wurde vom Server generiert
            game_config.code_is_coded = True

    def rate_moe(self):
        """
        Bewertet den aktuellen Zug des Spielers.
        """
        current_guess = game_config.board_final[game_config.current_row]

        string_guess = ""

        # Umwandeln des Rateversuchs in einen String
        for num in current_guess:
            string_guess += str(num)

        # Senden eines Requests an den Server, um den Rateversuch zu bewerten
        self.send_request(self.gameid, self.gamerid, self.positions, self.colors, string_guess)

        # Zählen der Anzahl von weißen und schwarzen Pins in der Antwort
        white_pins = self.value.count('7')
        black_pins = self.value.count('8')

        if white_pins is config.COLUMNS:
            # Der Spieler hat gewonnen
            game_config.player_won = True
            game_config.game_is_over = True
            game_config.solution = game_config.board_final[game_config.current_row]

        return black_pins, white_pins

    def send_request(self, gameid, gamerid, positions, colors, value):
        """
        Sendet eine Anfrage an einen Server mit den bereitgestellten Daten.

        Args:
            gameid (int): Die Spiel-ID.
            gamerid (str): Der Name des Spielers.
            positions (int): Die Anzahl der Positionen.
            colors (int): Die Anzahl der Farben.
            value (str): Der Wert.

        Returns:
            int: Die aktualisierte Spiel-ID.

        Raises:
            requests.exceptions.RequestException: Bei einem Fehler während der Anfrage.
        """
        global response
        url = "http://{}:{}".format(game_config.IP_ADDRESS, game_config.PORT)

        data = {
            "gameid": gameid,
            "gamerid": gamerid,
            "positions": positions,
            "colors": colors,
            "value": value
        }

        headers = {"Content-Type": "application/json"}

        try:
            # Senden einer POST-Anfrage an den Server
            response = requests.post(url, data=json.dumps(data), headers=headers)
            response_data = response.json()
            response.raise_for_status()

            if response.status_code == 200:
                # Extrahieren der Antwortdaten
                self.gameid = response_data.get("gameid", gameid)
                self.value = response_data["value"]

        except requests.exceptions.RequestException as e:
            print("Fehler beim Senden der Anfrage:", str(e))
            if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 400:
                response_data = e.response.json()
                error_message = response_data.get("error")
                if error_message:
                    print("Fehlermeldung vom Server:", error_message)
