from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open("commands.json", "r") as file:
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