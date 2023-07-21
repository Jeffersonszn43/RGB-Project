from gpiozero import LED
from time import sleep

#We are going from lsb to msb
W = LED(17) #Pin 11
X = LED(27) #Pin 13
Y = LED(22) #Pin 15
Z = LED(23) #Pin 16
	
while True:
      #Here we are asking the user to enter a color from the color wheel to display the number of that color.
      user_input = input("Please enter a color from the color wheel to display a number corresponding to that color: ")
      
      if user_input.lower() == 'black':
            Z.off()
            Y.off()
            X.off()
            W.off()
            print("Displaying the number 0!")

      elif user_input.lower() == 'green':
            Z.off()
            Y.off()
            X.off()
            W.on()
            print("Displaying the number 1!")

      elif user_input.lower() == 'blue':
            Z.off()
            Y.off()
            X.on()
            W.off()
            print("Displaying the number 2!")

      elif user_input.lower() == 'cyan':
            Z.off()
            Y.off()
            X.on()
            W.on()
            print("Displaying the number 3!")

      elif user_input.lower() == 'orange':
            Z.off()
            Y.on()
            X.off()
            W.off()
            print("Displaying the number 4!")

      elif user_input.lower() == 'yellow':
            Z.off()
            Y.on()
            X.off()
            W.on()
            print("Displaying the number 5!")

      elif user_input.lower() == 'red':
            Z.off()
            Y.on()
            X.on()
            W.off()
            print("Displaying the number 6!")

      elif user_input.lower() == 'white':
            Z.off()
            Y.on()
            X.on()
            W.on()
            print("Displaying the number 7!")
            
      else:
            print("The color you have chosen is not a color on the color wheel. Please enter a color on the color wheel.")
