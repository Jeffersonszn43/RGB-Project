from gpiozero import LED
from time import sleep
from gpiozero import AngularServo
#Here we are taking care of the jitter from the servo motor.
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory() 

# min_pulse_width converted from 500us to 0.0005s and max_pulse_width converted from 2400us to 0.0024s.
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
          Green.on()
          sleep(5)
          Green.off()

     elif user_input.lower() == 'blue':
          print("Displaying the color Blue.")
          servo.angle = 54
          Z.off()
          Y.off()
          X.on()
          W.off()
          Blue.on()
          sleep(5)
          Blue.off()

     elif user_input.lower() == 'cyan':
          print("Displaying the color Cyan.")
          servo.angle = 76
          Z.off()
          Y.off()
          X.on()
          W.on()
          Blue.on()
          Green.on()
          sleep(5)
          Blue.off()
          Green.off()

     elif user_input.lower() == 'orange':
          print("Displaying the color Orange.")
          servo.angle = 101
          Z.off()
          Y.on()
          X.off()
          W.off()
          Red.on()
          Yellow.on()
          sleep(5)
          Red.off()
          Yellow.off()
     
     elif user_input.lower() == 'yellow':
          print("Displaying the color Yellow.")
          servo.angle = 126
          Z.off()
          Y.on()
          X.off()
          W.on()
          Yellow.on()
          sleep(5)
          Yellow.off()

     elif user_input.lower() == 'red':
          print("Displaying the color Red.")
          servo.angle = 150
          Z.off()
          Y.on()
          X.on()
          W.off()
          Red.on()
          sleep(5)
          Red.off()

     elif user_input.lower() == 'white':
          print("Displaying the color White.")
          servo.angle = 180
          Z.off()
          Y.on()
          X.on()
          W.on()
          White.on()
          sleep(5)
          White.off()

     else:
          print("The color you have entered is not on the color wheel! Please enter a color that is on the color wheel: ")
         
         
