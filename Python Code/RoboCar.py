import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

forward = True
backward = False
speed = 100
gpio.setwarnings(False)

# Upper Left
U_L = 24
U_L_D = 12

gpio.setup(24, gpio.OUT) #DIR1
gpio.setup(12, gpio.OUT) #PWM1

#Upper Right
U_R = 21
U_R_D = 11

gpio.setup(21, gpio.OUT) #DIR2
gpio.setup(11, gpio.OUT) #PWM2

#Bottom Left
B_L = 23
B_L_D = 15

gpio.setup(23, gpio.OUT) #DIR1
gpio.setup(15, gpio.OUT) #PWM1

#Bottom Right
B_R = 26
B_R_D = 13

gpio.setup(26, gpio.OUT) #DIR2
gpio.setup(13, gpio.OUT) #PWM2
time.sleep(0.5)


#Creating the functions needed for easy steering of the Pi Car
def Forward():
    #Upper Left Forward
    gpio.output(U_L_D, backward)
    ulf = gpio.PWM(U_L, speed)
    ulf.start(50)

    #Upper Right Forward
    #gpio.output(U_R_D, backward)
    #urf = gpio.PWM(U_R, speed)
    #urf.start(50)
    
    #Bottom Left Forward
    #gpio.output(B_L_D, forward)
    #blf = gpio.PWM(B_L, speed)
    #blf.start(50)

    #Bottom Right Forward
    #gpio.output(B_R_D, forward)
    #brf = gpio.PWM(B_R, speed)
    #brf.start(50)


Forward()
time.sleep(2)
gpio.cleanup()