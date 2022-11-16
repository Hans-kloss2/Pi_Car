from flask import Flask
from flask import render_template, request
import RPi.GPIO as gpio
import time
gpio.cleanup()


app = Flask(__name__, template_folder='templates', static_folder='static')
gpio.setmode(gpio.BOARD)

forward = True
backward = False
speed = 250
gpio.setwarnings(False)

# Upper Left
U_L = 32  # PWM1
U_L_D = 23  # DIR1

gpio.setup(23, gpio.OUT)  # DIR1
gpio.setup(32, gpio.OUT)  # PWM1

# Upper Right
U_R = 33  # PWM2
U_R_D = 26  # DIR2

gpio.setup(26, gpio.OUT)  # DIR2
gpio.setup(33, gpio.OUT)  # PWM2

# Bottom Left
B_L = 15  # PWM1
B_L_D = 24  # DIR1

gpio.setup(24, gpio.OUT)  # DIR1
gpio.setup(15, gpio.OUT)  # PWM1

# Bottom Right
B_R = 13  # PWM2
B_R_D = 21  # DIR2

gpio.setup(21, gpio.OUT)  # DIR2
gpio.setup(13, gpio.OUT)  # PWM2


# Creating the functions needed for easy steering of the Pi Car
def UP():
    # Upper Left Forward
    gpio.output(U_L_D, forward)
    ulf = gpio.PWM(U_L, speed)
    ulf.start(80)

    # Upper Right Forward
    gpio.output(U_R_D, backward)
    urf = gpio.PWM(U_R, speed)
    urf.start(80)

    # Bottom Left Forward
    gpio.output(B_L_D, backward)
    blf = gpio.PWM(B_L, speed)
    blf.start(80)

    # Bottom Right Forward
    gpio.output(B_R_D, backward)
    brf = gpio.PWM(B_R, speed)
    brf.start(80)

def DOWN():
    # Upper Left Forward
    gpio.output(U_L_D, backward)
    ulf = gpio.PWM(U_L, speed)
    ulf.start(80)

    # Upper Right Forward
    gpio.output(U_R_D, forward)
    urf = gpio.PWM(U_R, speed)
    urf.start(80)

    # Bottom Left Forward
    gpio.output(B_L_D, forward)
    blf = gpio.PWM(B_L, speed)
    blf.start(80)

    # Bottom Right Forward
    gpio.output(B_R_D, forward)
    brf = gpio.PWM(B_R, speed)
    brf.start(80)

def LEFT():
    # Upper Left Forward
    gpio.output(U_L_D, backward)
    ulf = gpio.PWM(U_L, speed)
    ulf.start(80)

    # Upper Right Forward
    gpio.output(U_R_D, backward)
    urf = gpio.PWM(U_R, speed)
    urf.start(80)

    # Bottom Left Forward
    gpio.output(B_L_D, forward)
    blf = gpio.PWM(B_L, speed)
    blf.start(80)

    # Bottom Right Forward
    gpio.output(B_R_D, backward)
    brf = gpio.PWM(B_R, speed)
    brf.start(80)

def RIGHT():
    # Upper Left Forward
    gpio.output(U_L_D, forward)
    ulf = gpio.PWM(U_L, speed)
    ulf.start(80)

    # Upper Right Forward
    gpio.output(U_R_D, forward)
    urf = gpio.PWM(U_R, speed)
    urf.start(80)

    # Bottom Left Forward
    gpio.output(B_L_D, backward)
    blf = gpio.PWM(B_L, speed)
    blf.start(80)

    # Bottom Right Forward
    gpio.output(B_R_D, forward)
    brf = gpio.PWM(B_R, speed)
    brf.start(80)

def STOP():
    # Upper Left Forward
    gpio.output(U_L_D, backward)
    ulf = gpio.PWM(U_L, 0)
    ulf.start(0)

    # Upper Right Forward
    gpio.output(U_R_D, backward)
    urf = gpio.PWM(U_R, 0)
    urf.start(0)

    # Bottom Left Forward
    gpio.output(B_L_D, backward)
    blf = gpio.PWM(B_L, 0)
    blf.start(0)

    # Bottom Right Forward
    gpio.output(B_R_D, backward)
    brf = gpio.PWM(B_R, 0)
    brf.start(0)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'up':
            UP()
        elif request.form['submit_button'] == 'down':
            DOWN()
        elif request.form['submit_button'] == 'left':
            LEFT()
        elif request.form['submit_button'] == 'right':
            RIGHT()
        elif request.form['submit_button'] == 'stop':
            STOP()
    return render_template('index.html')





print ("Start")
app.run(host='0.0.0.0',port=5010)