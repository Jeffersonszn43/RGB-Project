from gpiozero import LED
from time import sleep
from gpiozero import AngularServo
#Here we are taking care of the jitter from the servo motor.
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory() 

servo = AngularServo(23, min_angle = 0, max_angle = 180, pin_factory = factory)  #Pin 16

#Here are the variables for the 7-Segment display. We are going from lsb to msb.
W = LED(17)  #Pin 11
X = LED(27)  #Pin 13
Y = LED(22)  #Pin 15
Z = LED(5)  #Pin 29

#Here are the variables for the LEDs.
Red = LED(6)   #Pin 31
Green = LED(26)  #Pin 37
Blue = LED(25)  #Pin 22
White = LED(16)   #Pin 36
Yellow = LED(24)   #Pin 18

while True:
     #Here we are asking the user to enter a color from the color wheel.
     user_input = input("Please enter a color from the color wheel:  ")

     if user_input.lower() == 'black':
          print("Displaying the color Black.")
          servo.angle = 0
          Z.off()
          Y.off()
          X.off()
          W.off()

     elif user_input.lower() == 'green':
          print("Displaying the color Green.")
          servo.angle = 33
          Z.off()
          Y.off()
          X.off()
          W.on()
          


