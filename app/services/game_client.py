from flask import Flask
import os
import requests


app = Flask(__name__)

GAME_SERVICE_URL = os.environ.get("GAME_SERVICE_URL", "http://127.0.0.1:5001/games")


def fetch_game_details(game_id):
    try:
        response = requests.get(f"{GAME_SERVICE_URL}/{game_id}")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        app.logger.error(f"Failed to fetch game {game_id}: {e}")
    return None
