from flask import Flask, Blueprint, jsonify, request
from app.services.game_client import fetch_game_details
import json
import os
import logging


app = Flask(__name__)

recommendation_bp = Blueprint("recommendations", __name__, url_prefix="/recommendations")

logging.basicConfig(level=logging.INFO)

# Load local database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '../data/recommendations.json')
with open(DATA_PATH, 'r') as f:
    recommendations = json.load(f)


def load_game_details(game_ids, k):
    app.logger.info("Accessing load_game_details.")
    return [fetch_game_details(gid) for gid in game_ids[:k] if fetch_game_details(gid)]


@recommendation_bp.route("/trending")
def get_trending():
    k = int(request.args.get("k", 5))
    return jsonify(load_game_details(recommendations.get("trending", []), k))


@recommendation_bp.route("/most_played")
def get_most_played():
    k = int(request.args.get("k", 5))
    return jsonify(load_game_details(recommendations.get("most_played", []), k))


@recommendation_bp.route("/top_categories")
def get_top_categories():
    k = int(request.args.get("k", 5))
    return jsonify(load_game_details(recommendations.get("top_categories", []), k))
