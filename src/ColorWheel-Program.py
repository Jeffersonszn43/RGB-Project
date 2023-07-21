from gpiozero import AngularServo
#Here we are taking care of the jitter from the servo motor.
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory() 

servo = AngularServo(17, min_angle = 0, max_angle = 180, pin_factory = factory)  #Pin 11

while True:
     #Here we are asking the user to enter a color on the wheel and depending on what color the user enters, the servo will turn to that color.
     user_input = input("Please enter a color on the color wheel to turn to that color:  ")

     if user_input.lower() == 'black':
          print("Turning to Black on the color wheel.")
          servo.angle = 0

     elif user_input.lower() == 'green':
          print("Turning to Green on the color wheel.")
          servo.angle = 27 

     elif user_input.lower() == 'blue':
          print("Turning to Blue on the color wheel.")
          servo.angle = 50

     elif user_input.lower() == 'cyan':
          print("Turning to Cyan on the color wheel.")
          servo.angle = 75

     elif user_input.lower() == 'orange':
          print("Turning to Orange on the color wheel.")
          servo.angle = 98  

     elif user_input.lower() == 'yellow':
          print("Turning to Yellow on the color wheel.")
          servo.angle = 120

     elif user_input.lower() == 'red':
          print("Turning to Red on the color wheel.")
          servo.angle = 145

     elif user_input.lower() == 'white':
          print("Turning to White on the color wheel.")
          servo.angle = 180

     else:
          print("That is not a valid color. Please select a color on the color wheel.")
