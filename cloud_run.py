#!/usr/bin/env python3
import os
from flask import Flask, jsonify, request, abort
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType
from bungie_api import BungieApi
import secret_config

config = secret_config.read()
cpk = config["discord"]["client_public_key"]
api = BungieApi(config["bungie"])

app = Flask(__name__)

@app.route('/interactions', methods=['POST'])
@verify_key_decorator(cpk)
def interactions():
  if request.json['type'] == InteractionType.APPLICATION_COMMAND:
    return jsonify({
        'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        'data': {
            'content': 'Hello world'
        }
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))