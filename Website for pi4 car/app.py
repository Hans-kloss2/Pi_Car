from flask import Flask
from flask import render_template, request
import RPi.GPIO as gpio
import time

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
time.sleep(0.5)


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
    time.sleep(0.2)

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
    time.sleep(0.2)

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
    time.sleep(0.2)

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
    time.sleep(0.2)

@app.route("/")

def index():
    return render_template('index.html')

@app.route('/')
def index():
    if form.validate_on_submit():
        if 'download' in request.form:
            pass # do something
        elif 'watch' in request.form:
            pass # do something else





print ("Start")

app.run(host='0.0.0.0',port=5010)

gpio.cleanup()