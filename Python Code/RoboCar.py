import RPi.GPIO as gpio
import time
gpio.cleanup()

gpio.setmode(gpio.BOARD)

forward = True
backward = False
speed = 100
gpio.setwarnings(False)

# Upper Left
U_L = 12 #PWM1
U_L_D = 23 #DIR1

gpio.setup(23, gpio.OUT) #DIR1
gpio.setup(12, gpio.OUT) #PWM1

#Upper Right
U_R = 11 #PWM2
U_R_D = 26 #DIR2

gpio.setup(26, gpio.OUT) #DIR2
gpio.setup(11, gpio.OUT) #PWM2

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


#Creating the functions needed for easy steering of the Pi Car
def Forward():
    #Upper Left Forward
    #ulf = gpio.PWM(U_L, speed)
    #ulf.start(50)
    #gpio.output(U_L_D, forward)

    #Upper Right Forward
    #urf = gpio.PWM(U_R, speed)
    #urf.start(50)
    #gpio.output(U_R_D, backward)
    
    #Bottom Left Forward
    blf = gpio.PWM(B_L, speed)
    blf.start(50)
    gpio.output(B_L_D, forward)

    #Bottom Right Forward
    #brf = gpio.PWM(B_R, speed)
    #brf.start(50)
    #gpio.output(B_R_D, forward)


Forward()
time.sleep(2)
gpio.cleanup()