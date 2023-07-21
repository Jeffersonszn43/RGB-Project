from gpiozero import LED
from time import sleep
from gpiozero import AngularServo
#Here we are taking care of the jitter from the servo motor.
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory() 

servo = AngularServo(23, min_angle = 0, max_angle = 180, pin_factory = factory)  #Pin 16

#We are going from lsb to msb
W = LED(17)
X = LED(27)
Y = LED(22)
Z = LED(23)

Red = LED(17)   #Pin 11
Green = LED(27)  #Pin 13
Blue = LED(22)  #Pin 15
White = LED(23)   #Pin 16
Yellow = LED(24)   #Pin 18

while True:
     #Here we are asking the user to enter a color on the wheel and depending on what color the user enters, the servo will turn to that color.
     user_input = input("Please enter a color on the color wheel to turn to that color:  ")

