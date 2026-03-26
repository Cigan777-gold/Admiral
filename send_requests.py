import time
import requests
from Status_system import Status_Server, System_Info, Cpu_Info, Ram_Info, Swap_Info

API_URL = "http://127.0.0.1:8080/api/stats/"
API_KEY = "f03cbdecb1b228b5ab020adad9f3263efbc21c8a2ee0f0c8d381dcf5e360ca95"

def collect_stats():
    return {
        "cpu": Status_Server()["cpu"],
        "ram": Status_Server()["ram"],
        # "IO": Status_Server()["IO"],
    }

while True:
    data = collect_stats()

    try:
        requests.post(
            API_URL,
            json=data,
            headers={"Authorization": f"Api-Key {API_KEY}"},
            timeout=5
        )
        print("sent:", data)
    except Exception as e:
        print("error:", e)

    time.sleep(10)