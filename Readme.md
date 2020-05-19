# Servo Motor controlled by Web API


# Idea

In this project, a servo motor is controlled by a computer which receives the
angles (to which to rotate the servo to) from a web server.

This is just a demonstrator to show, how to control an Arduino through a web
service.


# Setup

Install _Standard Firmata_ on an Arduino UNO.
You may need to install the Firmata library, then you can find that in
_Files > Examples > Firmata_.

Install the necessary dependencies for this project
(first two steps are optional -- only use those to set up a
[virtual environment](https://docs.python.org/3/tutorial/venv.html))

    python -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt


## Run locally

Then you can run the webserver using

    python webserver.py

and the controller for the Arduino using e.g.

    python arduino_controller.py http://localhost:5000 /dev/ttyACM0

The url, `localhost`, works if you run the webserver locally.


## Run with webserver in the cloud

You can get a free webserver that runs flask at e.g. https://www.pythonanywhere.com/
You can host the webserver there and change the url in the `arduino_controller.py` call.
