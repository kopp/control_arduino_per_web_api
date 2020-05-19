
from pyfirmata import Arduino, util
import requests
import time
import argparse


def get_angle_from_api(url_base):
    try:
        reply = requests.get(url_base + "/get_servo_angle", timeout=5)
    except requests.exceptions.Timeout:
        print("Timeout during request...")
        return 0
    try:
        return reply.json()["angle"]
    except KeyError:
        print("reply from API is not as expected.")
        return 0


def setup_board(usb_port, pin_number):
    board = Arduino(usb_port)
    servo_controller_pin = board.get_pin("d:{}:s".format(pin_number))  # s for servo
    print("Go...")
    return servo_controller_pin


def set_servo_from_api(servo_controller_pin, url_base):
    angle = get_angle_from_api(url_base)
    print("Rotating to angle {}".format(angle))
    servo_controller_pin.write(angle)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Set the servo motor angle to a value given by a web server."
    )
    parser.add_argument("url_base", help="Basepath of the webserver")
    parser.add_argument("usb_port", help="Name of the path/comport where the Arduino is connected to")
    parser.add_argument("--pin-number",
                        help="Number of the pin that is used to control the servo",
                        default=9,
                        )
    parser.add_argument("--sleep-duration",
                        help="Number of seconds to wait between consecutive servo angle changes.",
                        default=3,
                        )
    args = parser.parse_args()
    return args.url_base, args.usb_port, args.pin_number, args.sleep_duration


if __name__ == "__main__":
    url_base, usb_port, pin_number, sleep_duration = parse_arguments()
    servo_controller_pin = setup_board(usb_port, pin_number)
    while True:
        set_servo_from_api(servo_controller_pin, url_base)
        time.sleep(sleep_duration)
