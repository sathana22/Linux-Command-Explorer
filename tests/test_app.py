import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_grep_command():
    client = app.test_client()
    response = client.get("/api/commands/grep")

    assert response.status_code == 200

    data = response.get_json()

    assert data["description"] == "Search for patterns in files."
    assert "-i" in data["flags"]