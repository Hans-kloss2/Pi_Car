import rpi.GPIO as gpio

import time


gpio.setmode(gpio.BOARD)

gpio.setup(14, gpio.OUT) #DIR1

gpio.setup(1, gpio.OUT) #PWM1

gpio.output(14, True)

gpio.pwm(12, 50)

time.sleep(60)

gpio.cleanup()