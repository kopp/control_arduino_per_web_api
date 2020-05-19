
from flask import Flask, jsonify
import random


app = Flask(__name__)


@app.route("/get_servo_angle")
def get_servo_angle():
    angle = random.randint(0, 100)
    return jsonify(angle=angle)


if __name__ == "__main__":
    app.run(port=5000)
