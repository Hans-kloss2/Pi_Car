import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

forward = True
backward = False
speed = 230
gpio.setwarnings(False)

# Upper Left
U_L = 32 #PWM1
U_L_D = 23 #DIR1

gpio.setup(23, gpio.OUT) #DIR1
gpio.setup(32, gpio.OUT) #PWM1

#Upper Right
U_R = 33 #PWM2
U_R_D = 26 #DIR2

gpio.setup(26, gpio.OUT) #DIR2
gpio.setup(33, gpio.OUT) #PWM2

#Bottom Left
B_L = 15 #PWM1
B_L_D = 24 #DIR1

gpio.setup(24, gpio.OUT) #DIR1
gpio.setup(15, gpio.OUT) #PWM1

#Bottom Right
B_R = 13 #PWM2
B_R_D = 21 #DIR2

gpio.setup(21, gpio.OUT) #DIR2
gpio.setup(13, gpio.OUT) #PWM2
time.sleep(0.5)


#Creating the functions needed for easy steering of the Pi Car
def Forward():
    #Upper Left Forward
    gpio.output(U_L_D, forward)
    ulf = gpio.PWM(U_L, 230)
    ulf.start(50)

    #Upper Right Forward
    gpio.output(U_R_D, forward)
    urf = gpio.PWM(U_R, 230)
    urf.start(50)
    
    #Bottom Left Forward
    gpio.output(B_L_D, forward)
    blf = gpio.PWM(B_L, 230)
    blf.start(50)
    
    #Bottom Right Forward
    gpio.output(B_R_D, forward)
    brf = gpio.PWM(B_R, 230)
    brf.start(50)


#Forward()
gpio.output(U_L_D, True)
ulf = gpio.PWM(U_L, speed)
ulf.start(50)

time.sleep(2)


gpio.cleanup()