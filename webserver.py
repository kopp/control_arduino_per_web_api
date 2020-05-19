
from flask import Flask, jsonify
import requests
import random


MATHJS_API_URL = "https://api.mathjs.org/v4/"


app = Flask(__name__)


@app.route("/get_servo_angle")
def get_servo_angle():
    angle_a = random.randint(0, 50)
    angle_b = random.randint(0, 50)
    response = requests.get(MATHJS_API_URL, params={"expr": "{} + {}".format(angle_a, angle_b)})
    if response.ok:
        angle = int(response.content)
    else:
        angle = 1
    return jsonify(angle=angle)


if __name__ == "__main__":
    app.run(port=5000)
