import requests
import json

API_URL = "http://your-server/api/register/"
INSTALL_TOKEN = "SECRET123"


def register():
    response = requests.post(API_URL, json={
        "name": "server-1",
        "install_token": INSTALL_TOKEN
    })

    data = response.json()

    if "api_key" in data:
        with open("config.json", "w") as f:
            json.dump(data, f)

        print("Registered! API key saved.")
    else:
        print("Error:", data)


if __name__ == "__main__":
    register()