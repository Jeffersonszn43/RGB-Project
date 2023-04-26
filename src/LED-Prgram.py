from gpiozero import LED
from time import sleep

Red = LED(17)   #Pin 11
Green = LED(27)  #Pin 13
Blue = LED(22)  #Pin 15
White = LED(23)   #Pin 16
Yellow = LED(24)   #Pin 18

while True:
        #Here we are asking the user to enter a color they want to see from the color wheel.
        user_input = input("Please enter a color you want to see light up from the color wheel: ")

        if user_input.lower() == 'black':
            print("Displaying the color Black.")

        elif user_input.lower() == 'green':
             print("Displaying the color Green.")
             Green.on()
             sleep(4)
             Green.off()

        elif  user_input.lower() == 'blue':
              print("Displaying the color Blue.")
              Blue.on()
              sleep(4)
              Blue.off()
        elif  user_input.lower() == 'cyan':
              print("Displaying the color Cyan.")
              Blue.on()
              Green.on()
              sleep(4)
              Blue.off()
              Green.off()

        elif  user_input.lower() == 'orange':
              print("Displaying the color Orange.")
              Red.on()
              Yellow.on()
              sleep(4)
              Red.off()
              Yellow.off()

        elif  user_input.lower() == 'yellow':
              print("Displaying the color Yellow.")
              Yellow.on()
              sleep(4)
              Yellow.off()

        elif  user_input.lower() == 'red':
              print("Displaying the color Red.")
              Red.on()
              sleep(4)
              Red.off()

        elif  user_input.lower() == 'white':
              print("Displaying the color White.")
              White.on()
              sleep(4)
              White.off()

        else:
              print("Color is not found on the color wheel. Please enter a color that is on the color wheel.")
