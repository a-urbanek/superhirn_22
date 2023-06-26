import requests
import json
from config import game_config
from config import config
import numpy as np

IP_ADDRESS = "127.0.0.1"
PORT = 8001


class ComputerNetworkCoder:
    def __init__(self):
        self.gameid = 0
        self.gamerid = "Gruppe 22"
        self.positions = config.COLUMNS
        self.colors = len(config.COLORS)
        self.value = ""
        self.send_request(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        print("Game ID:", self.gameid)

        if self.gameid != 0:
            game_config.code_is_coded = True

    def rate_moe(self):
        """
        Bewertet den aktuellen Zug des Spielers.
        """
        # print(game_config.solution)
        # self.solution_temp = game_config.solution.copy()
        current_guess = game_config.board_final[game_config.current_row]
        # self.red_pins = self.count_red_pins()
        # self.white_pins = self.count_white_pins()


        # print("Number of white pins:", self.white_pins)
        # print("Number of red pins:", self.red_pins)

        # game_config.computer_is_playing = False
        # game_config.current_row -= 1

        string_guess = ""

        for num in current_guess:
            string_guess += str(num)

        self.send_request(self.gameid, self.gamerid, self.positions, self.colors, string_guess)

        white_pins = self.value.count('7')
        black_pins = self.value.count('8')

        if white_pins is config.COLUMNS:
            game_config.player_won = True
            game_config.game_is_over = True
            game_config.solution = game_config.board_final[game_config.current_row]

        # print(game_config.solution)
        return black_pins, white_pins

    def send_request(self, gameid, gamerid, positions, colors, value):
        """
        Sends a request to a server with the provided data.

        Args:
            gameid (int): The game ID.
            gamerid (str): The player's name.
            positions (int): The number of positions.
            colors (int): The number of colors.
            value (str): The value.

        Returns:
            int: The updated game ID.

        Raises:
            requests.exceptions.RequestException: If there is an error during the request.
        """

        global response
        url = "http://{}:{}".format(IP_ADDRESS, PORT)

        data = {
            "gameid": gameid,
            "gamerid": gamerid,
            "positions": positions,
            "colors": colors,
            "value": value
        }

        headers = {"Content-Type": "application/json"}

        try:
            # Send POST request to the server
            # print(json.dumps(data))
            response = requests.post(url, data=json.dumps(data), headers=headers)
            response_data = response.json()
            response.raise_for_status()

            if response.status_code == 200:
                # print("Request sent successfully.")
                # print("Sent data:", json.dumps(data))

                # Extract response data
                self.gameid = response_data.get("gameid", gameid)
                self.value = response_data["value"]


        except requests.exceptions.RequestException as e:
            print("Error sending the request:", str(e))
            if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 400:
                response_data = e.response.json()
                error_message = response_data.get("error")
                if error_message:
                    print("Server error message:", error_message)

# coder = ComputerNetworkCoder()
# coder.send_request(coder.gameid, coder.gamerid, coder.positions, coder.colors, "12345")
# print(coder.value)
# coder.send_request(coder.gameid, coder.gamerid, coder.positions, coder.colors, "12345")
# print(coder.value)
# coder.send_request(coder.gameid, coder.gamerid, coder.positions, coder.colors, "12345")
# print(coder.value)