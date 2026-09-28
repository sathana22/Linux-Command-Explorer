from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
commands_file = os.path.join(base_dir, "commands.json")

with open(commands_file, "r") as file:
    commands = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/commands")
def get_commands():
    return jsonify(commands)

@app.route("/api/commands/<command_name>")
def get_command(command_name):
    command = commands.get(command_name)

    if command:
        return jsonify(command)

    return jsonify({"error": "Command not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)