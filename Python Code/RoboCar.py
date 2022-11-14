import RPi.GPIO as gpio

import time



gpio.setmode(gpio.BOARD)

gpio.setup(23, gpio.OUT) #DIR1

gpio.setup(12, gpio.OUT) #PWM1


gpio.output(23, True)

p = gpio.PWM(12, 230)
p.start(50)

time.sleep(5)

gpio.cleanup()