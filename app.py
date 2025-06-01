from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/send')
def send_data():
    data = {
        "temperature": random.randint(20, 40),
        "gas": random.randint(100, 400),
        "smoke": random.randint(200, 600),
        "humidity": random.randint(30, 90),
        "vibration": random.randint(0, 10)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
