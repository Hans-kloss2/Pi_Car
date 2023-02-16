from flask import Flask
from flask import render_template, request
import RPi.GPIO as gpio
import time
gpio.cleanup()


app = Flask(__name__, template_folder='templates', static_folder='static')
gpio.setmode(gpio.BOARD)

forward = True
backward = False
gpio.setwarnings(False)


## Defining the Variables and setting the Pins to Output
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
    gpio.output(U_L, forward)

    # Upper Right Forward
    gpio.output(U_R_D, backward)
    gpio.output(U_R, forward)

    # Bottom Left Forward
    gpio.output(B_L_D, backward)
    gpio.output(B_L, forward)

    # Bottom Right Forward
    gpio.output(B_R_D, backward)
    gpio.output(B_R, forward)


def DOWN():
    # Upper Left Forward
    gpio.output(U_L_D, backward)
    gpio.output(U_L, forward)

    # Upper Right Forward
    gpio.output(U_R_D, forward)
    gpio.output(U_R, forward)

    # Bottom Left Forward
    gpio.output(B_L_D, forward)
    gpio.output(B_L, forward)

    # Bottom Right Forward
    gpio.output(B_R_D, forward)
    gpio.output(B_R, forward)


def LEFT():
    # Upper Left Forward
    gpio.output(U_L_D, backward)
    gpio.output(U_L, forward)

    # Upper Right Forward
    gpio.output(U_R_D, backward)
    gpio.output(U_R, forward)

    # Bottom Left Forward
    gpio.output(B_L_D, forward)
    gpio.output(B_L, forward)

    # Bottom Right Forward
    gpio.output(B_R_D, backward)
    gpio.output(B_R, forward)


def RIGHT():
    # Upper Left Forward
    gpio.output(U_L_D, forward)
    gpio.output(U_L, forward)

    # Upper Right Forward
    gpio.output(U_R_D, forward)
    gpio.output(U_R, forward)

    # Bottom Left Forward
    gpio.output(B_L_D, backward)
    gpio.output(B_L, forward)

    # Bottom Right Forward
    gpio.output(B_R_D, forward)
    gpio.output(B_R, forward)


def STOP():
    # Upper Left Forward
    gpio.output(U_L_D, backward)
    gpio.output(U_L, backward)

    # Upper Right Forward
    gpio.output(U_R_D, backward)
    gpio.output(U_R, backward)

    # Bottom Left Forward
    gpio.output(B_L_D, backward)
    gpio.output(B_L, backward)

    # Bottom Right Forward
    gpio.output(B_R_D, backward)
    gpio.output(B_R, backward)

# Driving left without rotating, hoepfully
def STILLLEFT():
    #gpio.output(U_L_D, forward)
    #gpio.output(U_L, forward)

    # Upper Right Forward
    gpio.output(U_R_D, forward)
    gpio.output(U_R, forward)

    # Bottom Left Forward
    #gpio.output(B_L_D, backward)
    #gpio.output(B_L, forward)

    # Bottom Right Forward
    #gpio.output(B_R_D, backward)
    #gpio.output(B_R, forward)


# Driving right without rotating, hoepfully
def STILLRIGHT():
    gpio.output(U_L_D, forward)
    gpio.output(U_L, forward)





# Flask implementation for recognizing the control of the Web interface
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
        elif request.form['submit_button'] == '<<':
            STILLLEFT()
        elif request.form['submit_button'] == '>>':
            STILLRIGHT()
    return render_template('index.html')



##############################################################
@app.route('/left.html')
def left():
    LEFT()
    return render_template('index.html')


@app.route('/right.html')
def right():
    RIGHT()
    return render_template('index.html')


@app.route('/up.html')
def up():
    UP()
    return render_template('index.html')


@app.route('/down.html')
def down():
    DOWN()
    return render_template('index.html')


@app.route('/space.html')
def space():
    STOP()
    return render_template('index.html')


@app.route('/stillleft.html')
def stillleft():
    STILLLEFT()
    return render_template('index.html')


@app.route('/stillright.html')
def stillright():
    STILLRIGHT()
    return render_template('index.html')

# Starting the webserver
print ("Start")
app.run(host='0.0.0.0',port=5010)

gpio.cleanup()