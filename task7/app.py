import os
import threading
import time
import requests
import random

from flask import Flask, request

PORT = int(os.environ["PORT"])
ANOTHER_APP_ADDRESS = os.environ["ANOTHER_APP_ADDRESS"]
app = Flask(__name__)

@app.route("/send_msg", methods=["POST"])
def send_message():
    msg = request.json.get('message_id')

    app.logger.info(msg)

    return ""


def post_something_on_another_app():
    time.sleep(5)
    post_url = f"{ANOTHER_APP_ADDRESS}/send_msg"

    message_id = 0
    while True:
        requests.post(post_url, json={"message_id": message_id})
        message_id += 1
        
        sleep_time = random.randint(1, 5)
        time.sleep(sleep_time)

if __name__ == "__main__":
    t = threading.Thread(target=post_something_on_another_app)
    t.start()

    app.run("0.0.0.0", PORT, app, use_reloader=False)
