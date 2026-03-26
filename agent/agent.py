import json
import time
import requests
import psutil

API_URL = "http://your-server/api/stats/"


def load_config():
    with open("config.json") as f:
        return json.load(f)


def get_stats():
    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent
    }


def main():
    config = load_config()

    while True:
        headers = {
            "Authorization": f"Api-Key {config['api_key']}"
        }

        requests.post(API_URL, json=get_stats(), headers=headers)

        time.sleep(60)


if __name__ == "__main__":
    main()